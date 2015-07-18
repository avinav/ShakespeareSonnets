import Tokenizer.tokenize as tk
import numpy as np

class JaccardIndex:
    def __init__(self, docMap, docSpace):
        self.docMap = docMap
        self.docSpace = docSpace
          
    def query(self, search_text):
        word_list = search_text.split()
        term_list = tk.tokenize(word_list)
        term_set = set(term_list)
        score_dict = {}
        for doc_id, doc_term_dict in self.docSpace.vector_dict.items():
            doc_term_set = set(list(doc_term_dict.keys()))
            termInt = len (term_set & doc_term_set)
            termUni = len (term_set | doc_term_set)
            if termUni == 0:
                ji = 0
            else :
                ji = float(termInt) / float(termUni)
            score_dict[doc_id] = ji
        return score_dict
    
    def result_tag(self, score_dict, thresh = -1):
        score = np.array(list(score_dict.values()))
        ind = np.argmax(score)
        if (score[ind] < thresh):
            return "NA"
        doc_id = list(score_dict.keys())[ind]
        return self.docMap[doc_id].name
        
        

    
            
            
          
        
