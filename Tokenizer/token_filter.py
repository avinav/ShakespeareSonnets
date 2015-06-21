import re

class Token_Filter_SC:
    exp = r"[^A-Za-z0-9]+"
       
    def consume(self, word_list):
        new_word_list = []
        for word in word_list:
            new_word_list.append(re.sub(Token_Filter_SC.exp, "", word))
        return new_word_list
    
class Token_Filter_StopWords:
    f = open('../util/stopwords.txt','r')
    stop_words = set(f.readlines())
    f.close()
    
    def consume(self, word_list):
        word_list_set = set(word_list)
        new_word_list = list(word_list_set - Token_Filter_StopWords.stop_words)
        return new_word_list
    
