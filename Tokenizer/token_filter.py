import re
from nltk.stem.porter import PorterStemmer
import os

class Token_Filter_SC:
    exp = r"[^A-Za-z0-9]+"
       
    def consume(self, word_list):
        new_word_list = []
        for word in word_list:
            new_word_list.append(re.sub(Token_Filter_SC.exp, "", word))
        return new_word_list
    
class Token_Filter_StopWords:
    fname = os.path.join(os.path.dirname(__file__), '../util/stopwords.txt')
    f = open(fname,'r')
    stop_words = set(f.readlines())
    f.close()
    
    def consume(self, word_list):
        word_list_set = set(word_list)
        new_word_list = list(word_list_set - Token_Filter_StopWords.stop_words)
        return new_word_list
    
class Token_Filter_Stemmer:
    ps = PorterStemmer()
    
    def consume(self, word_list):
        new_word_list = []
        for word in word_list:
            new_word_list.append(self.ps.stem(word))
        return new_word_list  
        
class Token_Filter_LowerCase:
    def consume(self, word_list):
        return [word.lower() for word in word_list]
