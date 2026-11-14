"""Read-only checks of the delivered notes and the protected inputs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

root = Path(__file__).resolve().parent.parent
build = root / 'build'
repo = root.parent
literature = Path('/Users/Benjamin/Literature')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_new_or_generated(path, value):
    # These reports were created for these notes; no protected input is written.
    path.write_text(json.dumps(value, indent=2) + '\n')

source = (root / 'quiver-varieties-introduction.tex').read_text()
aux = (build / 'quiver-varieties-introduction.aux').read_text()
pdf_path = build / 'quiver-varieties-introduction.pdf'
pdf = json.loads(subprocess.check_output([
    'qpdf', '--json', '--json-key=qpdf', '--json-key=pages', str(pdf_path)]))
objects = pdf['qpdf'][1]
destinations = {}
links = []
for wrapped in objects.values():
    value = wrapped.get('value', {})
    if not isinstance(value, dict):
        continue
    names = value.get('/Names', [])
    for i in range(0, len(names), 2):
        destinations[names[i]] = names[i + 1]
    if value.get('/Subtype') == '/Link':
        links.append(value)

incoming = {}
bad_links = []
internal_links = 0
external_links = 0
for link in links:
    action = link.get('/A', {})
    if action.get('/S') == '/URI':
        external_links += 1
        continue
    target = action.get('/D', link.get('/Dest'))
    if target is None:
        bad_links.append(link)
        continue
    internal_links += 1
    if isinstance(target, str):
        incoming[target] = incoming.get(target, 0) + 1
        if target not in destinations:
            bad_links.append(target)

labels = {}
for match in re.finditer(
    r'\\newlabel\{((?:gloss|examples):[^}]+)\}\{\{[^}]*\}\{(\d+)\}\{.*?\}\{([^}]+)\}', aux
):
    labels[match[1]] = {'page': int(match[2]), 'destination': 'u:' + match[3]}

entries = json.loads((build / 'glossary-map.json').read_text())
entry_checks = []
for entry in entries:
    result = {'term': entry['term'], 'slug': entry['slug']}
    for prefix in ('gloss', 'examples'):
        label = labels[f"{prefix}:{entry['slug']}"]
        ref = destinations[label['destination']]
        target = objects['obj:' + ref]['value']['/D'][0]
        assert target == pdf['pages'][label['page'] - 1]['object']
        assert incoming[label['destination']] > 0
        result[prefix + '_page'] = label['page']
        result[prefix + '_destination_resolves_to_expected_page'] = True
        result[prefix + '_has_incoming_link'] = True
    entry_checks.append(result)

log = (build / 'quiver-varieties-introduction.log').read_text(errors='replace')
issues = [line for line in log.splitlines()
          if re.search(r'Warning|Overfull|Underfull|undefined|^!', line)]
examples_source = source.split('\\section{Examples Glossary}', 1)[1]
counts = {
    'pages': len(pdf['pages']),
    'glossary_definitions': len(re.findall(r'^\\glossentry\{', source, re.M)),
    'examples_glossary_entries': len(re.findall(r'^\\examplegloss\{', source, re.M)),
    'examples_in_examples_glossary': len(re.findall(r'^\\item\b', examples_source, re.M)),
    'exercises': source.count('\\begin{exercise}'),
    'resolved_internal_link_annotations': internal_links,
    'external_link_annotations': external_links,
}
assert counts['glossary_definitions'] == counts['examples_glossary_entries'] == 64
assert counts['examples_in_examples_glossary'] == 128
assert counts['exercises'] == 14
assert len(labels) == 128
assert not issues and not bad_links
qpdf_check = subprocess.run(['qpdf', '--check', str(pdf_path)], capture_output=True, text=True)
assert qpdf_check.returncode == 0
write_new_or_generated(root / 'glossary-and-build-validation.json', {
    'counts': counts,
    'tex_log_issues': issues,
    'unresolved_internal_links': bad_links,
    'qpdf_check_exit_code': qpdf_check.returncode,
    'pdf_sha256': sha(pdf_path),
    'glossary_entries': entry_checks,
    'scope': 'Checks compilation, PDF structure and link targets; mathematical review is described separately.',
})

baseline = json.loads((build / 'repository-baseline.json').read_text())
changed = []
missing = []
for relative, before in baseline.items():
    path = repo / relative
    if not path.is_file():
        missing.append(relative)
    elif sha(path) != before:
        changed.append(relative)

before_inventory = json.loads((build / 'literature-inventory-before.json').read_text())
after_inventory = {}
for path in literature.rglob('*'):
    if path.is_file():
        stat = path.stat()
        after_inventory[str(path.relative_to(literature))] = {
            'size': stat.st_size, 'mtime_ns': stat.st_mtime_ns}
changed_lit = [p for p in before_inventory.keys() & after_inventory.keys()
               if before_inventory[p] != after_inventory[p]]
missing_lit = sorted(before_inventory.keys() - after_inventory.keys())
added_lit = sorted(after_inventory.keys() - before_inventory.keys())
used = json.loads((build / 'used-source-hashes-baseline.json').read_text())
for row in used:
    row['sha256_at_delivery'] = sha(Path(row['path']))
    row['unchanged_at_delivery'] = row['sha256_at_delivery'] == row['sha256']
assert not changed and not missing
assert not changed_lit and not missing_lit and not added_lit
assert all(row['unchanged_at_delivery'] for row in used)
write_new_or_generated(root / 'preservation-check.json', {
    'repository_root': str(repo),
    'pre_existing_workspace_files_sha256_checked': len(baseline),
    'changed_pre_existing_workspace_files': changed,
    'missing_pre_existing_workspace_files': missing,
    'literature_root': str(literature),
    'literature_files_size_and_mtime_checked': len(before_inventory),
    'changed_literature_metadata': changed_lit,
    'missing_literature_files': missing_lit,
    'added_literature_files': added_lit,
    'consulted_literature_pdfs_sha256_checks': used,
    'scope': 'All pre-existing non-Git workspace files were SHA-256 checked. All Literature files were checked by path, size and modification time; the two consulted textbook PDFs were also SHA-256 checked. The entire Literature collection was not content-hashed.',
})
print(json.dumps({'counts': counts, 'preserved_workspace_files': len(baseline),
                  'unchanged_literature_inventory': len(before_inventory)}, indent=2))
