'''
Created on Jun 10, 2015

@author: avinav
'''
from Tokenizer.token_filter import Token_Filter_SC, Token_Filter_LowerCase,\
    Token_Filter_Stemmer
from Indexer.index import Term

def tokenize(word_list):
    lower_case = Token_Filter_LowerCase()
    sp_char = Token_Filter_SC()
    stemmer = Token_Filter_Stemmer()
    
    term_list = lower_case.consume(word_list)
    term_list = sp_char.consume(term_list)
    term_list = stemmer.consume(term_list)
    
    return term_list


def add_termMap(termMap, doc):
    term_list = doc.term_list
    term_set = set(term_list)
    for term in term_set:
        if (term in termMap.keys()):
            termMap[term].increment_docfreq()
        else :
            tObj = Term(term)
            termMap[term] = tObj
        
        