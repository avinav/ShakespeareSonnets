'''
Created on Jun 10, 2015

@author: avinav
'''
from Tokenizer.token_filter import token_filter_spec_char

def tokenize(word_list):
    sp_char = token_filter_spec_char()
    word_list = sp_char.consume(word_list)
    return word_list