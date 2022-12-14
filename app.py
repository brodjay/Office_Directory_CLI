# Version 5
#Additional Updates
# Added presearch in Update
# Added "Continue" to menu_or_exit()
# Added try and except statements

from operator import truediv
import mysql.connector
import time
import os


#@# Database - Connect to database

conn = mysql.connector.connect(
    host = "localhost",
    user = "cli_app",
    password = "admin",
    database = "users_db"
)


#@# Create Cursor

cursor = conn.cursor()

#@# Menu Selection Functions

def add_new():
    resume = "add_new"
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
    conn.commit()# Commits addition
    print("\nRows modified: " + str(cursor.rowcount))
    print("\nNew user added.")
    add_new_result = "SELECT * FROM users WHERE id=%s"
    id_new = (id,)
    cursor.execute(add_new_result,id_new)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row)) 
    menu_or_exit(resume)

def find_name():
    resume = "find_name"

    try:
        search= input("Enter first or last name to search: ")
    except:
        print("This is not a valid response. Please try again")
        time.sleep(2)
        os.system('clear')
        find_name()

    find = "SELECT * FROM users WHERE last_name = %s OR first_name = %s"
    value = (search,search)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row))
    menu_or_exit(resume)

def find_id():
    resume = "find_id()"

    try:
        search= input("Enter id number: ")
    except:
        print("This is not a valid response. Please try again")
        time.sleep(2)
        os.system('clear')
        find_id()
    
    find = "SELECT * FROM users WHERE id = %s"
    value = (search,)
    cursor.execute(find, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row) + "\n")
    menu_or_exit(resume)
    

def update():
    resume = "update"
    print("You selected to update an existing user.\n")    
    
    isRunning = True
    while isRunning:
        try:
            id = int(input("User id where changes will be made: "))
            isRunning = False
        except:
            print("This is not a valid response. Please try again")
            time.sleep(2)
            os.system('clear')
             
    value = (id,)
    search_sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(search_sql, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row))
    search = input("\nIs this the correct record? Continue with update? (y, n): ")

    if search == "y":
        field = input("What field do you want to update?: ")
    elif search == "n":
        update()
    update_sql = "Update users SET {} = %s WHERE id=%s".format(field)

    change = input("Enter your modification here: ")
    
    value = (change, id)
    cursor.execute(update_sql, value)
    conn.commit() # Commits addition
    print("\nRows modified: " + str(cursor.rowcount))
    print("\nExisting user record updated.")
    update_result = "SELECT * FROM users WHERE id=%s"
    id_new = (id,)
    cursor.execute(update_result,id_new)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row)) 
    menu_or_exit(resume)

def delete():
    resume = "delete"
    os.system('clear')
    print("You selected to delete a record")

    # Ask for id.
    try:
        id = int(input("\nSearch for id: "))
    except:
        print("This is not a valid response. Please try again")
        time.sleep(2)
        os.system('clear')
        delete()

    # Search for record before delete to verify.
    value = (id,)
    search_sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(search_sql, value)
    result = cursor.fetchall()
    for row in result:
        print("\n" + str(row))
    search = input("\nIs this the correct record? Continue with delete? (y, n): ")

    # If yes delete, else restart delete().
    if search == "y":
        delete_sql = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_sql, value)
        conn.commit()
        print("\nRows modified: " + str(cursor.rowcount))
        print("The record has been deleted.")
        menu_or_exit(resume)
    elif search == "n":        
        delete()
    else:
        print("Incorrect response. Please try again.")
        delete()
  
def goodbye():
    print("Closing application. Goodbye!")
    quit()

#@# Menu or Exit option after performing menu task.
def menu_or_exit(resume):
    try:
        response = int(input("\nContinue (1), Return to menu (2) or Exit (3)?: " ))
    except:
        print("This is not a valid response. Please try again")
        time.sleep(2)
        os.system('clear')
        menu_or_exit()

    if response == 1 or 2 or 3:
        if response == 1:
            eval(resume + "()")
        elif response== 2:
            menu_option()
        elif response ==3:
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
    
    try:
        menu = int(input("Please select from the option above:  "))
    except:
        print("This was incorrect. Please select the correct number.")
        time.sleep(2)
        menu_option()
    
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
   

#@# Start App
menu_option()