from gluon.custom_import import track_changes; track_changes(True)

import os
import csv
import json
import pickle

import pandas as pd
# import numpy as np
# from sklearn.linear_model import SGDClassifier
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer

def callme(text):

	moduledir = os.path.dirname(os.path.abspath('__file__'))
	trained = pickle.load(open(os.path.join(moduledir, 'applications/authorific/modules/moduledata/all_trained.p'), "rb"))
	count_vect = trained['music_count_vect']
	mod = trained['music_classifier_svm_fit']
	tfidf_transformer = trained['music_tfidf_transformer']
	test_counts = count_vect.transform(pd.Series([text]))
	test_tfidf = tfidf_transformer.transform(test_counts)
	predicted_svm2 = mod.predict(test_tfidf) 
	print predicted_svm2

	return(predicted_svm2[0])