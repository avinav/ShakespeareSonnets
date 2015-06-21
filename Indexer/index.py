'''
Created on Jun 12, 2015

@author: avinav
'''
from collections import Counter

class Index:
    def __init__(self):
        self.dictionary = {}
    
    def add_term(self, term, posting):
        if (term not in self.dictionary.keys()):
            self.dictionary[term] = [posting]
        else :
            plist = self.dictionary[term]
            plist.append(posting)
    
    def add_docVector(self, docSpace, doc_id):
        posting_bag = docSpace.get_posting_bag(doc_id)
        for posting in posting_bag:
            self.add_term(posting.term, posting)
            
    def add_docSpace(self, docSpace):
        for doc_id in docSpace.vector_dict.keys():
            self.add_docVector(docSpace, doc_id)
        
class DocSpace:
    def __init__(self):
        self.vector_dict = {}
        
    def add_document(self, doc_id, term_list):
        self.vector_dict[doc_id] = self.term_reduce(term_list) 
        
    def term_reduce(self, term_list):
        term_dict =  Counter(term_list)
        return term_dict
    
    def get_posting_bag(self, doc_id):
        if  (doc_id not in self.vector_dict.keys()):
            return []
        term_freq_dict = self.vector_dict[doc_id]
        posting_bag = []
        for key,value in term_freq_dict.items():
            pos = Posting(doc_id, key, value)
            posting_bag.append(pos)
        return posting_bag

class Posting:
    def __init__(self,  doc_id, term, tfreq):
        self.doc_id = doc_id
        self.term = term
        self.tfreq = tfreq
        
class Term:
    counter = -1
    def __init__(self, term_text):
        Term.counter += 1
        self.term_id = Term.counter
        self.term_text = term_text
        self.docfreq = 1
    def increment_docfreq(self):
        self.docfreq += 1
        
        
