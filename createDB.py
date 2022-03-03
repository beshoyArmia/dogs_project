import sqlite3 

#create database
con = sqlite3.connect("dogs.db")  
print("Database opened successfully")
#create table  
con.execute("""create table Dogs
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
           description TEXT NOT NULL,
            link TEXT NOT NULL)""")  
print("Table created successfully")  
con.close()

