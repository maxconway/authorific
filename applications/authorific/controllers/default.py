# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
import backend_functions
from gluon.custom_import import track_changes; track_changes(True)

def error():
    return dict()

def index():
	response.menu = [
		['Authorific', True, URL('first')],
		['Explanation', True, URL('second')]
	]
	if request.vars.text:
		session.text = backend_functions.callme(request.vars.text)
		# redirect(URL('second'))
	return dict()

def second():
	response.menu = [
		['Authorific', True, URL('first')],
		['Explanation', True, URL('second')]
	]
	return dict()

