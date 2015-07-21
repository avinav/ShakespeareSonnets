import pylab
import numpy as np
import matplotlib.pyplot as plt

def confusion_matrix(true_labels, pred_labels, labels):
    true_labels = np.array(true_labels)
    pred_labels = np.array(pred_labels)
    n = len(labels)
    norm_conf = np.zeros((n,n))
    norm_conf_string = np.zeros((n,n))
    for i,li in enumerate(labels):
        for j,lj in enumerate(labels):
            norm_conf[i][j] = 100*np.mean(pred_labels[true_labels == li] == lj)
            norm_conf_string[i][j] = "%.2f" % norm_conf[i][j]
    norm_conf = norm_conf.tolist()
    return norm_conf, norm_conf_string

def display_confusion_matrix(conf_matrix, conf_matrix_string, num_labels, labels, fig_title):
    num_labels = num_labels.reshape(num_labels.size)
    total_acc = np.average(np.diagonal(conf_matrix), weights = num_labels)
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    res = ax.imshow(np.array(conf_matrix), cmap = pylab.cm.jet, interpolation='nearest')
    ax.set_title(fig_title+", Total Accuracy:" + str(total_acc))
    ax.set_ylabel("true_class label")
    ax.set_xlabel("predicred_class label")
    for i, cas in enumerate(conf_matrix_string):
        for j, c in enumerate(cas):
            if c>0:
                plt.text(j-.3, i+.3, c, fontsize=12)
    labels.insert(0,'')
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    cb = fig.colorbar(res)
    pylab.savefig(fig_title+".png", format="png")
    #fig.show()

def getAccuracy(conf_matrix, num_labels):
    total_acc = np.average(np.diagonal(conf_matrix), weights = num_labels)
    return total_acc

def reduce_label_binary(labels, true_label):
    new_labels = []
    for label in labels:
        if (label == true_label):
            new_labels.append('1')
        else :
            new_labels.append('0')
    return new_labels

def roc_tpr_fpr(true_labels, pred_labels):
    true_labels = reduce_label_binary(true_labels,'NA')
    pred_labels = reduce_label_binary(pred_labels,'NA')
    labels = ['0','1']
    norm_conf, norm_conf_str = confusion_matrix(true_labels,pred_labels,labels)
    return float(norm_conf_str[0,0]),float(norm_conf_str[1,0])






