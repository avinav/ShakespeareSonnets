'''
Created on Jun 13, 2015

@author: avinav
'''
import pickle
from Indexer.index import Index, DocSpace
from util.Document import Document
data = pickle.load(open('data/data.p','r'))
docSpace = data['docSpace']
document_map = data['document_map']
index = data['index']

print "document_map"
for doc_id, doc in document_map.items():
    print doc_id, doc.name

print "docSpace"
for doc_id, term_freq_dict in docSpace.vector_dict.items():
    print doc_id,":",term_freq_dict


print "index"
print index.dictionary.keys()
for term, posting_list in index.dictionary.items():
    print term
    for posting in posting_list:
        print posting.doc_id, posting.tfreq
