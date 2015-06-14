'''
Created on Jun 10, 2015

@author: avinav
'''
from Tokenizer.token_filter import Token_Filter_SC

def tokenize(word_list):
    sp_char = Token_Filter_SC()
    term_list = sp_char.consume(word_list)
    return term_list