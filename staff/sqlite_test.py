import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
names = ", ".join()