#/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick! 
sys.setdefaultencoding('UTF8')

from bottle import route, request, run, template, debug
from os.path import exists
import sys
import time

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
    print 'post'
    write_content = request.forms.get('notes')
    print write_content

    if write_content == 'clear':
        with open('main.log', 'w') as f:
                    pass
    else:
            with open('main.log', 'a+') as f:
                    print 'open file'
                    nowtime = time.strftime("%y-%m-%d %H: %M: %S")
                    note_content = nowtime + '\t' + write_content + '\n'
                    f.write(note_content)

    mynote = read_text()
                     
    return template('neworld_note', note=mynote)


if __name__ == "__main__":
    #debug(True)
    #run(host='localhost', port=8080, reloader=True)
    run(host='localhost', port=8080)

