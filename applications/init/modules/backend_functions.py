# from gluon.custom_import import track_changes; track_changes(True)

import os
import csv
import json
import pickle

import pandas as pd
# import numpy as np
# from sklearn.linear_model import SGDClassifier
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer

moduledir = os.path.dirname(os.path.abspath('__file__'))
songs = pickle.load(open(os.path.join(moduledir, 'applications/init/modules/moduledata/songs_all_trained.p'), "rb"))
literature = pickle.load(open(os.path.join(moduledir, 'applications/init/modules/moduledata/literature_all_trained.p'), "rb"))
speeches = pickle.load(open(os.path.join(moduledir, 'applications/init/modules/moduledata/speeches_all_trained.p'), "rb"))
# old_songs = pickle.load(open(os.path.join(moduledir, 'applications/init/modules/moduledata/all_trained.p'), "rb"))


def use_model(text, trained):
	count_vect = trained['count_vect']
	mod = trained['classifier_svm_fit']
	tfidf_transformer = trained['tfidf_transformer']
	test_counts = count_vect.transform(pd.Series([text]))
	test_tfidf = tfidf_transformer.transform(test_counts)
	predicted_svm2 = mod.predict(test_tfidf) 

	return(predicted_svm2[0])

def predict_song(text):
	return(use_model(text,songs))

# def predict_literature(text):
	# return(use_model(text,literature))

def predict_speech(text):
	return(use_model(text,speeches))

def callme(text):
	return(use_model(text,old_songs))

