import Foundation
import AppKit
import PDFKit

let directory = URL(fileURLWithPath: CommandLine.arguments[1])
let document = PDFDocument(url: directory.appendingPathComponent("quiver-varieties-introduction.pdf"))!
let output = directory.appendingPathComponent("previews", isDirectory: true)
try FileManager.default.createDirectory(at: output, withIntermediateDirectories: true)
let selected = [1, 3, 8, 10, 11, 12, 14, 17, 19, 26, 37]
for number in selected {
    let page = document.page(at: number - 1)!
    let thumbnail = page.thumbnail(of: NSSize(width: 850, height: 1200), for: .mediaBox)
    let bitmap = NSBitmapImageRep(data: thumbnail.tiffRepresentation!)!
    try bitmap.representation(using: .png, properties: [:])!.write(
        to: output.appendingPathComponent(String(format: "page-%02d.png", number)))
}
var internalLinks = 0
var unresolvedLinks = 0
var replacementCharacters = 0
for index in 0..<document.pageCount {
    let page = document.page(at: index)!
    replacementCharacters += (page.string ?? "").filter { $0 == "\u{fffd}" }.count
    for annotation in page.annotations where annotation.type == "Link" {
        if annotation.action is PDFActionURL { continue }
        internalLinks += 1
        let destination = annotation.destination ?? (annotation.action as? PDFActionGoTo)?.destination
        if destination?.page == nil { unresolvedLinks += 1 }
    }
}
let report: [String: Any] = ["pages": document.pageCount,
                           "preview_pages": selected,
                           "internal_link_annotations": internalLinks,
                           "unresolved_internal_links": unresolvedLinks,
                           "text_replacement_characters": replacementCharacters]
let data = try JSONSerialization.data(withJSONObject: report, options: [.prettyPrinted, .sortedKeys])
try data.write(to: directory.appendingPathComponent("pdfkit-validation.json"))
print(String(data: data, encoding: .utf8)!)
