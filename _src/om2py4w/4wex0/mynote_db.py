#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

db=sqlite3.connect('mynote.db')
curs=conn. cursor()

db.execute('''CREATE TABLE mynote (time text, note_content text)''')
curs.execute("INSERT INTO mynote VALUES ('2015-11-16', 'hello')")

db.commit()
db.close()
