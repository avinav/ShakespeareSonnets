import re

class token_filter_spec_char:
    def __init(self):
        self.exp = r"[^A-Za-z0-9]+"
    def consume(self, word_list):
        new_word_list = []
        for word in word_list:
            new_word_list.append(re.sub(self.exp, "", word))
        return new_word_list