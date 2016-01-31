import os
import csv
import json
import pickle

import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer(use_idf=True, smooth_idf=True)

def callme(text):

	# mod = pickle.load(open("./moduledata/svm_classifier.p", "rb"))
	# count_vect = pickle.load(open("./moduledata/count_vect.p", "rb"))
	trained = pickle.load(open("./moduledata/all_trained.p", "rb"))
	test_counts = count_vect.transform(pd.Series(['baby baby more baby']))
	test_tfidf = tfidf_transformer.transform(test_counts)
	predicted_svm2 = mod.predict(test_tfidf) 
	print predicted_svm2

	return(predicted_svm2[0])