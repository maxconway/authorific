import os
import csv
import json
import pickle

import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier

def callme(text):

	x = pickle.load(open("./moduledata/svm_classifier.p", "rb"))

	predicted_svm2 = x.predict(test_tfidf) 
	print predicted_svm2

	return(text)