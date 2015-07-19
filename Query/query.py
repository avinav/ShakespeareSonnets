'''
Created on Jun 13, 2015

@author: avinav
'''

import Tokenizer.tokenize as tk
import math
import operator
import pickle

class QueryIndex:
    def __init__(self, index, docSpace, docMap, termMap):
        self.index = index
        self.docSpace = docSpace
        self.docMap = docMap
        self.termMap = termMap
        self.N = len(docMap.keys())
        print self.N
        
    def get_term_list(self, phrase):
        word_list = phrase.split()
        term_list = tk.tokenize(word_list)
        return term_list
    
    def fetch_posting_list(self, term):
        if (term in self.index.dictionary.keys()):
            return self.index.dictionary[term]
        else:
            return []
        
    def intersect_list(self, plist, docid_set, posting_bag):
        plist_docid = [pos.doc_id for pos in plist if pos is not None]
        if docid_set:
            res_set = docid_set.intersection(set(plist_docid))
        else :
            res_set = set(plist_docid)
        res_plist = [pos for pos in plist if pos.doc_id in res_set]
        posting_bag += res_plist
        return res_set, posting_bag
        
    def intersect_posting_list(self, pl_list):
        docid_set = None
        posting_bag = []
        for plist in pl_list:
            docid_set, posting_bag = self.intersect_list(plist, docid_set, posting_bag)
        return docid_set, posting_bag
    
    def query(self, phrase):
        term_list = self.get_term_list(phrase)
        pl_list = []
        for term in term_list:
            pl_list.append(self.fetch_posting_list(term))
        docid_set, posting_bag = self.intersect_posting_list(pl_list)
        score = self.vsm_score(term_list, docid_set)
        score_sorted = sorted(score.items(), key=operator.itemgetter(1))
        return score_sorted
    
    def vsm_score(self, term_list, docid_set, k = -1):
        k = len(docid_set) if(k == -1) else k
        ctr = 0
        score = {}
        for docid in docid_set:
            if ctr >= k:
                break
            docVector = self.docSpace.vector_dict[docid]
            score[docid] = 0
            norm_tf = 0
            norm_idf = 0
            for term in term_list:
                if term in self.termMap.keys():
                    tf = docVector[term]
                    tf = (1 + math.log(tf)) if (tf != 0) else 0
                    idf = float(self.N)/self.termMap[term].docfreq
                    idf = math.log(idf)
                    norm_tf += tf**2
                    norm_idf += idf**2
                    score[docid] += tf*idf
            score[docid] /= (math.sqrt(norm_tf)*math.sqrt(norm_idf))
            ctr += 1
        return score
    
def getQueryIndex(data_file):
    data = pickle.load(open(data_file,'r'))
    index = data['index']
    docSpace = data['docSpace']
    termMap = data['termMap']
    docMap = data['docMap']
    return QueryIndex(index, docSpace, docMap, termMap)
 
