#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

db=sqlite3.connect('con_note.db')
db.execute('''CREATE TABLE mynote (time text, note_content text)''')
db.execute("INSERT INTO mynote VALUES ('2015-11-16', 'hello,')")
db.execute("INSERT INTO mynote VALUES ('2015-11-16', 'who are you?')")
db.execute("INSERT INTO mynote VALUES ('2015-11-16', 'Where are you from?')")
db.commit()
db.close()
