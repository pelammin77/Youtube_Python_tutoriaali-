import PyPDF2
from nltk.tokenize import sent_tokenize


def get_text_from_pdf(fn, start_page=0):
    print(fn)
    pdfFileObj = open(fn, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.getPage(0)
    text = pages.extractText()
    pdfFileObj.close()
    return  text


def read_txt_file(fn):
    with open(fn,'r', encoding='utf-8') as f:
        text_list = f.readlines()

    text_str = ' '.join(text_list)
    text_str = text_str.upper()
    return text_str






def tokenize_text(text, toke='.'):
    sents = text.split(toke)
    return sents


def sent_tokenizer_text(text):
    sent_text =sent_tokenize(text)
    return  sent_text






def check_plagiarism(text1, text2):
    res_list = []
    for x in text1:
        for y in  text2:
            if x == y :
                res_list.append(x)

    print(len(text1), len(text2))
    print(len(res_list))
    return res_list

text = read_txt_file('text_1.txt')
text2 = read_txt_file('text_2.txt')
sents_1= sent_tokenizer_text(text)
sents_2= sent_tokenizer_text(text2)
check_plagiarism(sents_1, sents_2)







