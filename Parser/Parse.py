'''
Created on Apr 27, 2015

@author: avinav
'''

from Tokenizer.tokenize import tokenize
from util.Document import Document

def create_document(doc, doc_path):
    f = open(doc_path + "/" + doc.name, "w+")
    f.write('\n'.join(doc.term_list) + '\n')
    f.close()
    
def parse(name, content, doc_path = ""):
    word_list = []
    for line in content.split("\n"):
        for word in line.split():
            word_list.append(word)
    term_list = tokenize(word_list)
    doc = Document(name, term_list)
    if doc_path != "":
        create_document(doc, doc_path)
    return doc


    
    


#---- Reading configuration file

