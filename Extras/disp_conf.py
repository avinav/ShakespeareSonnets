import pickle
import Extras.RunnerExcel.confusion_matrix
import Extras.RunnerExcel.display_confusion_matrix


result = pickle.load(open('resultwithna.p','w'))
doc_names = ['R1','R3','R4','R5','R7','NA']
count_dict = Counter(true_labels)
num_labels = np.array([count_dict[lab] for lab in doc_names])
conf_matrix, conf_matrix_string = confusion_matrix(true_labels, result, doc_names)
display_confusion_matrix(conf_matrix, conf_matrix_string, num_labels, doc_names)

