'''
Created on Jun 12, 2015

@author: avinav
'''

class Index:
    def __init__(self):
        self.dictionary = {}
    def add_term(self, term, posting):
        plist = self.dictionary[str(term)]
        if (plist is None or plist.isEmpty()):
            self.dictionary[str(term)] = [posting]
        else :
            plist.append(posting)
        
class DocVector:
    def __init__(self):
        self.vector = {}
    def add_document(self, doc_id, term_list):
        term_tuple_list = reduce(term_list)
        self.vector[str(doc_id)] = term_tuple_list
    def reduce(self, term_list):
        term_tuple_list = []
        return term_tuple_list

class Posting:
    def __init__(self, doc_id, tfreq):
        self.doc_id = doc_id
        self.tfreq = tfreq
