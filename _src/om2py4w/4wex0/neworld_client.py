#/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick! 
sys.setdefaultencoding('UTF8')

from lxml import html
import requests   

def read_note():
    page = requests.get('http://localhost:8080/neworld')
    page.decoding = 'utf-8'
    tree = html.fromstring(page.content)
    note_content = tree.xpath('//div[@class="note_content"]/text()')

    return note_content

def write_note(mynote):
    wpage = requests.post('http://localhost:8080/neworld', data = {'notes': mynote})
   


def main():
    while True:
        mynote = raw_input('>>> ')
        
        mynote = mynote.decode('gbk')
        
        if mynote == "q":
            print ("Thanks for writing.")
            break
        elif mynote =="r":
            print read_note()
        else:
                write_note(mynote)

    

if __name__ == "__main__":
        main()
