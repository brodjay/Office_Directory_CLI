# Version 3 - 
#Completed updated()
#Fixed commit problem when making changes to the database.

import mysql.connector
import time
import os
import re


#@# Database - Connect to database

conn = mysql.connector.connect(
    host = "localhost",
    user = "cli_app",
    password = "admin",
    database = "users_db"
)


#@# Create Cursor and Commit objects

cursor = conn.cursor()
commit = conn.commit()

#cursor.execute("SHOW DATABASES")
#print("Database Connection Successful")

#@# Menu Selection Functions

def add_new():
    print("You selected to add a new person.\n")    
    add_new = "INSERT INTO users(id, first_name, last_name, gender, email, username, ip_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    id = int(input("Enter id: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    gender = input("Enter gender: ")
    username = input("Enter username: ")
    ip_address = input("Enter ip address: ")
    value = (id, first_name, last_name, gender, email, username, ip_address)
    cursor.execute(add_new, value)
    #commit
    conn.commit()# Commits addition
    print("\nRows modified: " + str(cursor.rowcount))
    print("\nNew user added.")
    add_new_result = "SELECT * FROM users WHERE id=%s"
    id_new = (id,)
    cursor.execute(add_new_result,id_new)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row)) 
    menu_or_exit()

def find_name():
    search= input("Enter first or last name to search: ")
    find = "SELECT * FROM users WHERE last_name = %s OR first_name = %s"
    value = (search,search)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row))
    menu_or_exit()

def find_id():
    search= input("Enter id number: ")
    find = "SELECT * FROM users WHERE id = %s"
    value = (search,)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row) + "\n")
    menu_or_exit()
    

def update():
    print("You selected to update an existing user.\n")    
    
    id = int(input("User id where changes will be made: "))

    field = input("What field do you want to update?: ")
    update = "Update users SET {} = %s WHERE id=%s".format(field)

    change = input("Enter your modification here: ")
    
    value = (change, id)
    cursor.execute(update, value)
    conn.commit() # Commits addition
    print("\nRows modified: " + str(cursor.rowcount))
    print("\nExisting user record updated added.")
    update_result = "SELECT * FROM users WHERE id=%s"
    id_new = (id,)
    cursor.execute(update_result,id_new)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row)) 
    menu_or_exit()

def delete():
    print("You selected to delete a record")
    quit()

def goodbye():
    print("Closing application. Goodbye!")
    quit()

#@# Menu or Exit option after performing menu task.
def menu_or_exit():
    try:
        response = int(input("\nReturn to menu (1) or Exit (2)?: " ))
    except:
        print("This is not a valid response. Please try again")
        time.sleep(2)
        os.system('clear')
        menu_or_exit()

    if response == 1 or 2:
        if response == 1:
            print("")
            menu_option()
        elif response== 2:
            goodbye()
        else:
            print("This is not a valid response. Please try again")
            time.sleep(2)
            os.system('clear')
            menu_or_exit()

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