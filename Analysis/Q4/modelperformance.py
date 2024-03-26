# modelperformance.py      By: Samer Al-khateeb
# This code is a modified version of the code provided here: 
# https://machinelearningmastery.com/how-to-calculate-precision-recall-f1-and-more-for-deep-learning-models/

# demonstration of calculating metrics for a our model
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
import pandas as pd


listOfFiles = ['cyber-Eq1.csv', 'cyber-Eq2.csv',
				'physical-Eq1.csv', 'physical-Eq2.csv',
				'combined-Eq1.csv','combined-Eq2.csv']


for csvFileName in listOfFiles:
	csvFileContentAsDataFrame = (pd.read_csv(csvFileName))
	# file columns
	mobID = csvFileContentAsDataFrame['MobID']
	trueClasses = csvFileContentAsDataFrame['TrueClassForMeetupMobs']
	predictedSimulationClasses = csvFileContentAsDataFrame['PredictedSimulationClass']
	#the true class values
	testy = trueClasses
	#the predicted class values
	yhat_classes = predictedSimulationClasses

	print("Processing File: ", csvFileName)
	
	# explanation for the Classification Metrics
	# https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
	# accuracy: (tp + tn) / (p + n)
	accuracy = accuracy_score(testy, yhat_classes)
	print('Accuracy: %f' % accuracy)

	# precision tp / (tp + fp)
	precision = precision_score(testy, yhat_classes)
	print('Precision: %f' % precision)
	# recall: tp / (tp + fn)
	recall = recall_score(testy, yhat_classes)
	print('Recall: %f' % recall)
	# f1: 2 tp / (2 tp + fp + fn)
	f1 = f1_score(testy, yhat_classes)
	print('F1 score: %f' % f1)

	# kappa
	kappa = cohen_kappa_score(testy, yhat_classes)
	print('Cohens kappa: %f' % kappa)

	# confusion matrix
	matrix = confusion_matrix(testy, yhat_classes)
	print("Confusion Matrix:")
	print(matrix)

	print()
	print()
	'''
	# ROC AUC
	auc = roc_auc_score(testy, yhat_probs)
	print('ROC AUC: %f' % auc)
	'''



