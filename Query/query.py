'''
Created on Jun 13, 2015

@author: avinav
'''

import Tokenizer.tokenize as tk
class QueryIndex:
    def __init__(self, index, docSpace, docMap):
        self.index = index
        self.docSpace = docSpace
        self.docMap = docMap
        
    def get_term_list(self, phrase):
        word_list = phrase.split()
        term_list = tk.tokenize(word_list)
        return term_list
    
    def fetch_posting_list(self, term):
        if (term in self.index.dictionary.keys()):
            return self.index.dictionary[term]
        else:
            return []
    
    def query(self, phrase):
        term_list = self.get_term_list(phrase)
        
