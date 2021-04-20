#!C:/Users/HP/AppData/Local/Programs/Python/Python39/python.exe
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi 
import sqlite3

form = cgi.FieldStorage()
movieid = form.getvalue("movieid")
moviename = form.getvalue("moviename")
postername = form.getvalue("postername")
year = form.getvalue("year")
genre = form.getvalue("genre")
rating = form.getvalue("rating")

db = sqlite3.connect("bookyourshow.db")
cursor = db.execute("SELECT * FROM MOVIES WHERE ID = \'"+movieid+"\';")
info = list(cursor)
if(info):
    print("<h1>Movie already exists</h1>")
    print("<br>")
    print("<a href='../bookyourshow/add_movie.html'>")
    print("<button>Go back</button>")
    print("</a>")
else:
    db.execute("INSERT INTO MOVIES VALUES("+movieid+", '"+moviename+"', '"+postername+"', "+year+", '"+genre+"', "+rating+");")
    db.commit()
    print("<h1>"+moviename+" added succesfully!</h1>")
    print("<br>")
    print("<a href='../bookyourshow/manage_movies.html'>")
    print("<button>Go back</button>")
    print("</a>")
db.close()