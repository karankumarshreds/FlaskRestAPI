import sqlite3
import os 

URI = str(os.getenv("SQL_URI"))

connection = sqlite3.connect(URI)

cursor = connection.cursor()


## CREATE A TABLE 
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

## INSERT SINGLE
user = (1, "Karan", "asdf")
insert_query = F"INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

## INSERT MANY
users = [
    (1, "Karan", "asdf"),
    (2, "Kajol", "asdf"),
    (3, "Luke", "asdf")
]
cursor.executemany(insert_query, users)

connection.commit()
connection.close()