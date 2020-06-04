import sqlite3
import os

print(os.path.isfile('MoviesList_SQL.db'))


"""
con = sqlite3.connect('database1.db')  # assigning to "con" value connection to "MovieList.db" database
con.row_factory = sqlite3.Row  # access to to records of database by indexs and NAMES
cur = con.cursor()  # creating and assigning "cursor" methods to "cur" value



"""