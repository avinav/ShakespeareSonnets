'''
Created on Jun 13, 2015

@author: avinav
'''
import pickle
from Indexer.index import Index, DocSpace
from util.Document import Document
data = pickle.load(open('util/index_data.p','r'))
docSpace = data['docSpace']
docMap = data['docMap']
index = data['index']
termMap = data['termMap'] 

print "docMap"
for doc_id, doc in docMap.items():
    print doc_id, doc.name
print" termMap"
for term,tObj in termMap.items():
    print term, tObj.docfreq
#     
# print "docSpace"
# for doc_id, term_freq_dict in docSpace.vector_dict.items():
#     print doc_id,":",term_freq_dict


# print "index"
# print index.dictionary.keys()
# for term, posting_list in index.dictionary.items():
#     print term
#     for posting in posting_list:
#         print posting.doc_id, posting.tfreq
