'''
Created on Apr 27, 2015

@author: avinav
'''

import requests
from bs4 import BeautifulSoup
from Parser import Parse
import Tokenizer.tokenize 

def crawl(url, index, docSpace, document_map, termMap, **kwargs):
    doc_path = kwargs.get('doc_path')
    atags = getChildren(url)
    i = 0
    for atag in atags:
#         if ( i == 1):
#             break
        name = atag.content
        nexturl = url + atag['href']
        r = requests.get(nexturl)
        soup = BeautifulSoup(r.text)
        content = soup.find_all('tr')[1].td
        # Remove br from content
        for e in content.find_all('br'):
            e.extract()
        doc = Parse.parse(atag['href'], content.text, doc_path)
        Tokenizer.tokenize.add_termMap(termMap, doc)
        document_map[doc.id] = doc
        # add code to add term_id/term_text, term_object in term_map
    
        docSpace.add_document(doc.id, doc.term_list)
        index.add_docVector(docSpace, doc.id)
        i += 1
    print i
    
def getChildren(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    trows = soup.find_all('tr')
    atags = trows[1].find_all('a')
    return atags
    

