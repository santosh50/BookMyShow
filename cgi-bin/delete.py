#!C:/Users/HP/AppData/Local/Programs/Python/Python39/python.exe
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi 
import sqlite3

form = cgi.FieldStorage()
movieid = form.getvalue("movieid")

db = sqlite3.connect("bookyourshow.db")
cursor = db.execute("SELECT * FROM MOVIES WHERE ID = \'"+movieid+"\';")
info = list(cursor)
if(not info):
    print("<h1>Movie does not exist</h1>")
    print("<br>")
    print("<a href='../bookyourshow/delete_movie.html'>")
    print("<button>Go back</button>")
    print("</a>")
else:
    moviename = info[0][1]
    db.execute("DELETE FROM MOVIES WHERE ID =\'"+movieid+"\';")
    db.commit()
    print("<h1>"+moviename+" deleted succesfully!</h1>")
    print("<br>")
    print("<a href='../bookyourshow/manage_movies.html'>")
    print("<button>Go back</button>")
    print("</a>")