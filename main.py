import pyttsx3
import PyPDF2

book = open("object_oriented_python_tutorial.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()