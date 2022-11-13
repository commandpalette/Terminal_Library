## Importing Modules
from pubsub import pub
# import Views.login_form
from Views.login_form import Login_form
import Models.database
import Models.calculations
from tkinter import messagebox
from Views.dashboard import Dashboard


# Importing Done
message_string = "Library - Manager"


## Functions related to the login page
# Check login credentials and  call the Dashboard if successful
def login_data(login_data):
    username  = login_data.split(",")[0]
    password = login_data.split(",")[1]
    result  = Models.database.login_check(username, password)
    if result:
        books_taken = Models.database.books_taken(username)
        book_lending_list = Models.database.book_lending()
        book_taken_list = Models.database.book_details(username)
        whole_book = []
        whole_book = book_taken_list
        book_lending_list  = Models.calculations.book_taken_data(book_lending_list)
        book_taken_list  = Models.calculations.book_taken_data(book_taken_list)
        name.killing_app()
        calling_dashboard(username , books_taken , book_taken_list , book_lending_list , whole_book)
    else:
        messagebox.showerror(message_string , "Wrong username or password")

        

## Functions related to the registration page
# Call the registration page and call the Dashboard if successful
def registration_data(registration_data):
    username  = registration_data.split(",")[0]
    password = registration_data.split(",")[1]
    result  = Models.database.registration_check(username , password)
    if result:
        messagebox.showinfo(message_string , "Registration Successful")
    else:
        messagebox.showerror(message_string , "User Already Exists - Choose Different Username and Password")

""" Rent Book Data """
def rent_book(book_name):
    returned_data = Models.database.book_lending_database(book_name)
    # pub.sendMessage("returned_books" , book_details = returned_data)
    # db.inserting_data_into_table
    db.inserting_data_after_rent_click(returned_data)

    

## Calling the required login forms and Dashboard
# Login form
def calling_login():
    global name
    name  = Login_form()
    name.non_dynamic_controls()
    name.placing_controls()
    name.calling_app()
# Dashboard form
def calling_dashboard(username , bookcount , *book_details):
    global db
    db =Dashboard(username ,bookcount , *book_details)
    db.defining_static_controls()
    db.defining_dynamic_controls()
    db.placing_controls()

"""Pub Message's for calling diff fuctions"""
# Pub messages from the Login form
pub.subscribe(login_data , "login_data")
pub.subscribe(registration_data , "registration_data")
pub.subscribe(rent_book , "book_renting")



if __name__ == '__main__':
    calling_login()
   # calling_dashboard("vinay" , 0)
