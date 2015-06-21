import Tokenizer.tokenize as tk
import numpy as np

class JaccardIndex:
    def __init__(self, docSpace, docMap):
        self.docSpace = docSpace
        self.docMap = docMap
          
    def query(self, search_text):
        word_list = search_text.split()
        term_list = tk.tokenize(word_list)
        term_set = set(term_list)
        score_dict = {}
        for doc_id, doc_term_dict in self.docSpace.items():
            doc_term_set = set(list(doc_term_dict.keys()))
            termInt = len (term_set & doc_term_set)
            termUni = len (term_set | doc_term_set)
            ji = float(termInt) / float(termUni)
            score_dict[doc_id] = ji
        return doc_id
    
    def result_tag(self, score_dict):
        score = np.array(list(score_dict.values()))
        ind = np.argmax(score)
        doc_id = list(score_dict.keys())[ind]
        return self.docMap[doc_id].name
        
        

    
            
            
          
        