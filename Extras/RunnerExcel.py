import xlrd
import Parser.Parse as Parse
from Indexer.index import DocSpace
from Extras.jaccardIndex import JaccardIndex
import pickle
import numpy as np
from collections import Counter
from Extras.confusion_matrix import *
import matplotlib.pyplot as plt
import pylab

def get_docSpace_excel(filename, sheetname, col_no):
    docMap = {}
    docSpace = DocSpace()
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(sheetname)
#     num_rows = worksheet.nrows - 1
    num_rows = 5
    curr_row = 0
    doc_names = ['R1','R3','R4','R5','R7']
    while curr_row < num_rows:
        text = worksheet.cell_value(curr_row, col_no)
#         doc = Parse.parse("Rumor" + str(curr_row), text)
        doc = Parse.parse(doc_names[curr_row], text)
        docMap[doc.id] = doc
        docSpace.add_document(doc.id, doc.term_list)
        curr_row += 1
    return docMap, docSpace

def get_tweet_excel(filename, sheetname, col_no):
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(sheetname)
    num_rows = worksheet.nrows 
    print "num rows:",num_rows
    curr_row = 0
    search_text_list = []
    while curr_row < num_rows:
        text = worksheet.cell_value(curr_row, col_no)
        if "http:" in text:
            text = text.split("http:")[0]
        search_text_list.append(text)
        curr_row += 1   
    return search_text_list
        
def query_list(search_text_list, docMap, docSpace, thresh = -1):
    jIndex = JaccardIndex(docMap, docSpace)
    result = []
    print "thresh here:",thresh
    for search_text in search_text_list:
        score_dict = jIndex.query(search_text)
        result.append(jIndex.result_tag(score_dict,thresh))
    return result, score_dict

#------- script starts here

rumor_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"
tweet_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"
thresh = 0.0068
# f = open(tweet_filename, 'r')
# search_text_list = f.readlines().split("\n")
docMap, docSpace = get_docSpace_excel(rumor_filename, "Rumor Examples", 2)
search_text_list = get_tweet_excel(tweet_filename, "test_jaccard", 2)
true_labels = get_tweet_excel(tweet_filename,"test_jaccard",3)
#print "search text list: ", search_text_list
#print "docSpace: ", docSpace.vector_dict

# FOR ROC
'''
tpr_list = []
fpr_list = []
thresh_list = np.arange(0,0.2,0.001)
for thresh in thresh_list:
    result, score_dict = query_list(search_text_list, docMap, docSpace,thresh)
    print "thresh:",thresh
    tpr, fpr = roc_tpr_fpr(true_labels, result)
    print "tpr, fpr: ", tpr,fpr
    tpr_list.append(tpr)
    fpr_list.append(fpr)
pickle.dump({'tpr':tpr_list,'fpr':fpr_list},open('tpr_fpr.p','w'))
fig = plt.figure()
plt.plot(fpr_list, tpr_list,marker='o')
ax = plt.gca()
#i = 0
#for xy in zip(fpr_list, tpr_list): 
#    thresh = thresh_list[i]
#    print thresh
#    ax.annotate(str(thresh), xy=xy, textcoords='data')
plt.title("JACCARD ROC CURVE")
plt.xlabel("FPR of Rumour")
plt.ylabel("TPR of Rumour")
pylab.savefig("roc_curve_jaccard.png",format="png")
'''


# For displaying confusion matrix
result, score_dict = query_list(search_text_list, docMap, docSpace,thresh)
#print "score ", score_dict
#pickle.dump(result, open('resultwithna.p','w'))
#print "\n".join(result)
doc_names = ['R1','R3','R4','R5','R7','NA']
count_dict = Counter(true_labels)
num_labels = np.array([count_dict[lab] for lab in doc_names])
conf_matrix, conf_matrix_string = confusion_matrix(true_labels, result, doc_names)
tpr,fpr = roc_tpr_fpr(true_labels,result)
print tpr,fpr
display_confusion_matrix(conf_matrix, conf_matrix_string, num_labels, doc_names,"Jacc_" +str(thresh))
data = {'num_labels' : num_labels, 'conf_matrix':conf_matrix, 
        'conf_matrix_string':conf_matrix_string, 'true_labels':true_labels,
        'pred_labels':result, 'doc_names':doc_names}

pickle.dump(data,open('confwithna.p','w'))
