#!C:/Users/HP/AppData/Local/Programs/Python/Python39/python.exe
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi 
import sqlite3
import hashlib

form = cgi.FieldStorage()
username = form.getvalue("uname")
password = form.getvalue("pwd")
passwordHash = hashlib.sha256(password.encode()).hexdigest()

db = sqlite3.connect("bookyourshow.db")
cursor = db.execute("SELECT * FROM MANAGERS WHERE Username = \'"+username+"\';")
info = list(cursor)
if(not info):
    print("<h1>Invalid Username</h1>")
    print("<br>")
    print("<a href='../bookyourshow/manager_login.html'>")
    print("<button>Try Again</button>")
    print("</a>")
elif(passwordHash != info[0][1]):
    print("<h1>Incorrect Password</h1>")
    print("<br>")
    print("<a href='../bookyourshow/manager_login.html'>")
    print("<button>Try Again</button>")
    print("</a>")
else:
    print("<script>")
    print("window.location.replace('../bookyourshow/manage_movies.html?uname="+username+"&flag=1')")
    print("</script>")
db.close()