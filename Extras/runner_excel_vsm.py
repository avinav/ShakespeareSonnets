from RunnerExcel import get_docSpace_excel
from RunnerExcel import get_tweet_excel
from RunnerExcel import query_list_vsm
from Query.query import QueryIndex
from collections import Counter
from Extras.confusion_matrix import *
from RunnerExcel import generate_roc_curve
import operator
import pickle

rumor_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"
tweet_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"

# docMap, docSpace, termMap, index = get_docSpace_excel(rumor_filename, "Rumor Examples", 2)
# search_text_list = get_tweet_excel(tweet_filename, "test_jaccard", 2)
# true_labels = get_tweet_excel(tweet_filename,"test_jaccard",3)

data = pickle.load(open('rumour.p','r'))
docMap = data['docMap']
docSpace = data['docSpace']
termMap = data['termMap']
index = data['index']
search_text_list = data['search_text_list']
true_labels = data['true_labels']
queryIndex = QueryIndex(index, docSpace, docMap, termMap)
# pickle.dump({'docMap':docMap, 'docSpace':docSpace, 
#              'termMap':termMap, 'index':index, 
#              'search_text_list':search_text_list, 'true_labels':true_labels},open('rumour.p','w'))
thresh = 0.6
# thresh_list  = np.arange(0,4,0.1);
# generate_roc_curve(search_text_list, docMap, queryIndex, thresh_list, true_labels, "VSM_ROC_CURVE")
pred_labels = query_list_vsm(search_text_list, docMap, queryIndex, thresh)
 
doc_names = ['R1','R3','R4','R5','R7','NA']
count_dict = Counter(true_labels)
num_labels = np.array([count_dict[lab] for lab in doc_names])
conf_matrix, conf_matrix_string = confusion_matrix(true_labels, pred_labels, doc_names)
tpr,fpr = roc_tpr_fpr(true_labels,pred_labels)
print thresh
print tpr,fpr
acc = getAccuracy(conf_matrix, num_labels)
print acc, np.average(np.array(pred_labels) == np.array(true_labels))
print "---------------"
# # display_confusion_matrix(conf_matrix, conf_matrix_string, num_labels, doc_names,"VSM_" +str(thresh))
