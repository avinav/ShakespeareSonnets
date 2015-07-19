import pickle

from Query.query import QueryIndex

data = pickle.load(open('util/index_data.p','r'))
index = data['index']
docMap = data['docMap']
termMap = data['termMap']
docSpace = data['docSpace']

queryIndex = QueryIndex(index, docSpace, docMap, termMap)
f = open('util/search_phrases.txt','r')
search_list = [phrase.split('\n')[0] for phrase in f.readlines()]
f.close()
print search_list
fw = open('util/output.txt','a')
for phrase in search_list:
    score = queryIndex.query(phrase)
    fw.write(str(score) +'\n')
    print score
    
fw.write('--------------------------\n')
fw.close()