# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:27:07 2016

@author: kurner

A namedtuple is a subclass of tuple allowing for named
columns and therefore dot notation access, treating 
elements as named attributes.

Bookmark(place='Anaconda.org', url='http://anaconda.org')
"""

from collections import namedtuple
import sqlite3 as sql

Bmk = namedtuple('Bookmark', ['place', 'url'])

# tuple of tuples
tuples = (
    ("Anaconda.org", "http://anaconda.org"),
    ("Python.org", "http://python.org"),
    ("Python Docs", "https://docs.python.org/3/"),
    ("Spaghetti Code", "http://c2.com/cgi/wiki?SpaghettiCode"),
    ("Structured Programming", "http://c2.com/cgi/wiki?StructuredProgramming"),
    ("XKCD", "http://xkcd.com"),
    ("CodeAcademy: Python","https://www.codecademy.com/learn/python"),
    ("Unicode on Youtube", "https://www.youtube.com/watch?v=Z_sl99D2a18"),
    ("In Defense of Ada", "http://www.grunch.net/synergetics/adaessay.html"),
    ("Grace Hopper on Letterman", "https://www.youtube.com/watch?v=1-vcErOPofQ"),
    ("The Mind of a Genius: John von Neumann", "https://www.youtube.com/watch?v=XZ9tt72feL8"),
    ("Warriors of the Net", "https://www.youtube.com/watch?v=PBWhzz_Gn10"),
    ("LAMP stack", "https://www.google.com/search?q=lamp+stack&safe=off&biw=787&bih=535&source=lnms&tbm=isch"),
    ("LAMP stack (Wikipedia)","https://en.wikipedia.org/wiki/LAMP_(software_bundle)"),
)

def main():
    # lets make these namedtuples instead OK?
    # *tup explodes each tuple into two positionals, what Bmk expects
    bookmarks = [Bmk(*tup) for tup in tuples] # list comprehension!
        
    for bmk in iter(bookmarks[:5]):
        # Bookmark(place='Anaconda.org', url='http://anaconda.org')
        print(f"{bmk.place:30} {bmk.url:20}")  # notice format of output: __repr__
    
    # login
    conn = sql.connect("./data/bookmarks.db")
    curs = conn.cursor()
    
    # https://www.sqlite.org/lang_droptable.html
    # DB API ???
    curs.execute("""DROP TABLE IF EXISTS Bookmarks""")
    curs.execute("""CREATE TABLE Bookmarks
        (bk_place text PRIMARY KEY,
         bk_url text)""")
    
    for bmk in sorted(bookmarks):
        query = ("INSERT INTO Bookmarks " 
        "(bk_place, bk_url) "
        "VALUES ('{}', '{}')".format(bmk.place, bmk.url))
        # print(query)
        curs.execute(query)
        conn.commit()
    
    # challenge:  instead of writing to a text file, write to a SQLite DB
    # using sqlite3.  Two column table:  e.g. place, url
    conn.close()

if __name__ == "__main__":
    main()