import numpy as np
import pickle
import matplotlib.pyplot as plt
from pylab import *
from  Extras.confusion_matrix import *
data = pickle.load(open('confwithna.p','rb'))
true_labels = data['true_labels']
pred_labels = data['pred_labels']
num_labels = data['num_labels']
doc_names = data['doc_names']
#conf_matrix = data['conf_matrix']
#conf_matrix_string = data['conf_matrix_string']
print doc_names
#conf_matrix, conf_matrix_string = confusion_matrix(true_labels,pred_labels, doc_names)
#display_confusion_matrix(conf_matrix, conf_matrix_string, num_labels, doc_names,"Jaccard")
tpr,fpr = roc_tpr_fpr(true_labels,pred_labels)
print tpr,fpr

