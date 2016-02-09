# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
# import pandas as pd
import backend_functions

def error():
    return dict()

def index():
	response.menu = [
		['Authorific', True, URL('index')],
		['Explanation', True, URL('explanation')]
	]
	if request.vars.text:
		# session.text = backend_functions.callme(request.vars.text)
		session.song = backend_functions.predict_song(request.vars.text)
		session.literature = backend_functions.predict_literature(request.vars.text)
		session.speech = backend_functions.predict_speech(request.vars.text)
		# redirect(URL('second'))
	return dict()

def second():
	response.menu = [
		['Authorific', True, URL('index')],
		['Explanation', True, URL('explanation')]
	]
	return dict()

