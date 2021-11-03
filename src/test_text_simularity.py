import nltk
nltk.download()

#import PyPDF2


def get_text_from_pdf(fn, start_page=0):
    print(fn)
    pdfFileObj = open(fn, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.getPage(0)
    text = pages.extractText()

    print(text)

    return  text


text1 = get_text_from_pdf('plagi_1.pdf')
print(text1)








