import pyttsx3
import PyPDF2

book = open('Module  7 -DIM_acs.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(3,pages):
    page = pdfReader.getPage(3)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

