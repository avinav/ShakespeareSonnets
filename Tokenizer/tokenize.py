'''
Created on Jun 10, 2015

@author: avinav
'''
from Tokenizer.token_filter import Token_Filter_SC, Token_Filter_LowerCase,\
    Token_Filter_Stemmer

def tokenize(word_list):
    lower_case = Token_Filter_LowerCase()
    sp_char = Token_Filter_SC()
    stemmer = Token_Filter_Stemmer()
    
    term_list = lower_case.consume(word_list)
    term_list = sp_char.consume(term_list)
    term_list = stemmer.consume(term_list)
    
    return term_list