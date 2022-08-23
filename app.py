# Version 1 - Connecetd to DB; Created Curor; Created Menu; Created Find by name and by id functions.

import mysql.connector
import time
import re


#@# Database - Connect to database

conn = mysql.connector.connect(
    host = "localhost",
    user = "dba",
    password = "adminadmin",
    database = "users_db"
) 

#@# Create Cursor

cursor = conn.cursor()
#cursor.execute("SHOW DATABASES")
#print("Database Connection Successful")

#@# Menu Selection Placeholders

def add_new():
    print("You selected add a new person")
    quit()

def find_name():
    search= input("Enter first or last name to search: ")
    find = "SELECT * FROM users WHERE last_name = %s OR first_name = %s"
    value = (search,search)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print(row)

def find_id():
    search= input("Enter id number: ")
    find = "SELECT * FROM users WHERE id = %s"
    value = (search,)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print(row)
    

def update():
    print("You selected to update a record")
    quit()

def delete():
    print("You selected to delete a record")
    quit()

def goodbye():
    print("Closing application. Goodbye")
    quit()

#@# Menu Function
def menu_option():
    print('''
    Menu\n
    =============================\n
    1. Add a new name.\n
    2. Find a person by name.\n
    3. Find a person by id.\n
    4. Update a persons information.\n
    5. Delete a person by ID.\n
    6. Quit Application\n''')

    menu = int(input("Please select from the option above:  "))
    if menu == 1:
        add_new()
    elif menu == 2:
        find_name()
    elif menu == 3:
        find_id()    
    elif menu == 4:
        update()
    elif menu == 5:
        delete()
    elif menu == 6:
        goodbye()
    else:
        print("This was incorrect. Please select the correct number")
        time.sleep(3)
        menu_option()

#@# Start App
menu_option()