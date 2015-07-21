import xlrd
import Parser.Parse as Parse
from Indexer.index import DocSpace
from Extras.jaccardIndex import JaccardIndex
import Tokenizer
from Indexer.index import Index
import numpy as np
import operator
from Extras.confusion_matrix import *

def get_docSpace_excel(filename, sheetname, col_no):
    docMap = {}
    termMap = {}
    index = Index()
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
        Tokenizer.tokenize.add_termMap(termMap, doc)
        docMap[doc.id] = doc
        docSpace.add_document(doc.id, doc.term_list)
        index.add_docVector(docSpace, doc.id)
        curr_row += 1
    return docMap, docSpace, termMap, index

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
        
def query_list_jacc(search_text_list, docMap, docSpace, thresh = -1):
    jIndex = JaccardIndex(docMap, docSpace)
    result = []
    print "thresh here:",thresh
    for search_text in search_text_list:
        score_dict = jIndex.query(search_text)
        result.append(jIndex.result_tag(score_dict,thresh))
    return result

def query_list_vsm(search_text_list, docMap, queryIndex, thresh = -1):
    docid_set = set(docMap.keys())
    pred_labels = []
    for text in search_text_list:
        term_list = queryIndex.get_term_list(text)
        score = queryIndex.vsm_score(term_list, docid_set)
        score_sorted = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
        if len(score_sorted) > 0:
            if score_sorted[0][1] < thresh:
                pred_labels.append('NA')
            else :            
                pred_labels.append(docMap[score_sorted[0][0]].name)
        else :
            pred_labels.append('NA')
    return pred_labels

def generate_roc_curve(search_text_list, docMap, queryIndex, thresh_list, true_labels, fig_title):
#     thresh_list = np.arange(0,0.2,0.001)
    tpr_list = []
    fpr_list = []
    for thresh in thresh_list:
        result = query_list_vsm(search_text_list, docMap, queryIndex,thresh)
        tpr, fpr = roc_tpr_fpr(true_labels, result)
        tpr_list.append(tpr)
        fpr_list.append(fpr)
    fig = plt.figure()
    plt.plot(fpr_list, tpr_list,marker='o')
    ax = plt.gca()
    #i = 0
    #for xy in zip(fpr_list, tpr_list): 
    #    thresh = thresh_list[i]
    #    print thresh
    #    ax.annotate(str(thresh), xy=xy, textcoords='data')
    plt.title(fig_title)
    plt.xlabel("FPR of Rumour")
    plt.ylabel("TPR of Rumour")
    pylab.savefig(fig_title + ".png",format="png")