#/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, route, request, run, template
from time import localtime, strftime
import sys
import sqlite3 #录入数据尚未成功


def read_text(): 
        f = open('main.log', 'a+')
        return f.read()
    
def write_text():
    f = open('main.log', 'a+')
    edit_time= strftime("%Y %b %d %H:%M:%S", localtime())
    f.write('%s     %s\n' %(edit_time, newnote))
    f.close()


@route('/neworld')
def neworld():
           mynote = read_text()
           return template('neworld_note', note=mynote)
    

@route('/neworld', method='POST')
def write_note():
     write_content = request.forms.get('write_content')
     write_text(write_content)
     mynote=read_text()
     return template('neworld', note=mynote)

@route('/read')
def read_from_url():
    return read_note()


run(host='localhost', port=8080, debug=True)
