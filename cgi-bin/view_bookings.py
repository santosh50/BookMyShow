#!C:/Users/HP/AppData/Local/Programs/Python/Python39/python.exe
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi 
import sqlite3

db = sqlite3.connect("bookyourshow.db")
cursor = db.execute("SELECT * FROM BOOKINGS;")
bookings = list(cursor)

print("<title>Browse Movies</title>")
print("<style>")
print("h1 {text-align: center; font-family: 'Courier New', Courier, monospace; padding: 40;}")
print(".large {font-size: x-large; font-weight: bold; padding: 40; font-family: 'Courier New', Courier, monospace;}")
print("b { padding-right: 20}")
print(".flex-container { display: flex; font-size: 25; font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;}")
print(".button0 { background-color: yellow; color: black; padding: 20.0; text-align: center; font-size: large; border-radius: 10px; cursor: pointer;}")
print("</style>")
print("<body bgcolor='lightskyblue'>")
print("<a href='../bookyourshow/home_page.html'>")
print("<button class='button0'>Back</button></a>")
print("<h1>Your Bookings</h1>")
print("<hr>")

for i in range(len(bookings)):
    print("<div class='flex-container'>")
    print("<div>")
    print("<p class='large'>"+str(i+1)+". </p>")
    print("</div>")
    print("<div>")
    print("<b>Movie: </b>"+bookings[i][0]+"<br>")
    print("<b>Time: </b>"+bookings[i][2]+"<br>")
    print("<b>Tickets: </b>"+str(bookings[i][1])+"<br>")
    print("<b>Price: </b>"+bookings[i][3]+"<br>")
    print("</div>")
    print("</div>")
    print("<hr>")