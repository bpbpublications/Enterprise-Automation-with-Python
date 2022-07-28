import docx

document = docx.Document("test_doc.docx")

for para in document.paragraphs:
    print(para.text)
