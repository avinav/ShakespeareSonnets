from RunnerExcel import get_docSpace_excel
from RunnerExcel import get_tweet_excel
from RunnerExcel import query_list_jacc
from Extras.confusion_matrix import *
from collections import Counter
import pickle


rumor_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"
tweet_filename = "../util/Rumor Coding_Intercoder_Round3_Eval5.xlsx"
thresh = 0.0068
# f = open(tweet_filename, 'r')
# search_text_list = f.readlines().split("\n")
docMap, docSpace, termMap, index = get_docSpace_excel(rumor_filename, "Rumor Examples", 2)
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
result = query_list_jacc(search_text_list, docMap, docSpace,thresh)
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
