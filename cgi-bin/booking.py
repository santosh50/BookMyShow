#!C:/Users/HP/AppData/Local/Programs/Python/Python39/python.exe
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi 
import sqlite3

form = cgi.FieldStorage()
moviename = form.getvalue("name")
ticketCount = str(form.getvalue("ticket"))
showtime = form.getvalue("time")
price = form.getvalue("price")

db = sqlite3.connect("bookyourshow.db")
db.execute("INSERT INTO BOOKINGS VALUES('"+moviename+"', "+ticketCount+", '"+showtime+"', '"+price+"');")
db.commit()

print("<title>Confirmation</title>")
print("<style>")
print("h1 {text-align: center; font-family: 'Courier New', Courier, monospace; padding: 40;}")
print("div {text-align: center; padding: 40;}")
print("button { background-color: yellow; color: black; text-align: center; padding: 40.0; font-size: 20; cursor: pointer; border-radius: 16px}")
print("</style>")
print("<body bgcolor='lightskyblue'>")
print("<h1>Booking Confirmed!</h1>")
print("<div>")
print("<a href='../bookyourshow/home_page.html'>")
print("<button>Back to Home Page</button>")
print("</a>")
print("</div>")

