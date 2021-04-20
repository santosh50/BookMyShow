import sqlite3
import hashlib

# db = sqlite3.connect('bookyourshow.db')
# print("opened database successfully")
db = sqlite3.connect("bookyourshow.db")
#CREATE TABLE
# db.execute('''CREATE TABLE BOOKINGS (
#     Name    VARCHAR(100)    NOT NULL,
#     Tickets INT NOT NULL,
#     Showtime   VARCHAR(10)    NOT NULL,
#     Price    VARCHAR(50) NOT NULL
# );''')
# print("created")

#INSERT VALUES INTO MOVIES
# db.execute('''INSERT INTO MOVIES
#     VALUES(55, 'Interstellar', 'interstellar.jpg', 2014, 'Science Fiction', 8.6);
# ''')
# db.commit()
# print("inserted")

#INSERT VALUES INTO USERS
# db.execute('''INSERT INTO USERS
# #     VALUES('abc', 'c5ae5f176fadad3c9fe337ac7d4846b2603faffc66dfa47295d638021671a547', 'abc@gmail.com', '09-12-2012', 9876543210);
# # ''')
# db.commit()
# print("inserted")

#DROP TABLE
# db.execute("DROP TABLE BOOKINGS;")

#DELETE
# db.execute("DELETE FROM BOOKINGS;")
# db.commit()

# moviename = 'Tenet'
# ticketCount = '5'
# showtime = '12:00 PM'
# price = "Rs. 2500/-"
# db.execute("INSERT INTO BOOKINGS VALUES('"+moviename+"', "+ticketCount+", '"+showtime+"', "+price+");")

# cursor = db.execute("SELECT * FROM USERS")
# print(list(cursor))