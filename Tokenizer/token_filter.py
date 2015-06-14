import re

class Token_Filter_SC:
    exp = r"[^A-Za-z0-9]+"   
    def consume(self, word_list):
        new_word_list = []
        for word in word_list:
            new_word_list.append(re.sub(Token_Filter_SC.exp, "", word))
        return new_word_list