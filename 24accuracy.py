# 24accuracy.py by Anisha Patel

def data(tp, fp, tn, fn):
	accuracy = (tp + tn) / (tp + tn + fp + fn)
	precision = (tp) / (tp + fp)
	recall = (tp) / (tp + fn)
	F1 = (2 * precision * recall) / (precision + recall)
	return accuracy, F1
	
print("(accuracy,F1)", data(1, 2, 3, 4)) 
print("(accuracy,F1)", data(2, 3, 4, 5)) 
print("(accuracy,F1)", data(11213, 23243, 343241, 442341)) 
 