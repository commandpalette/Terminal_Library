# Welcome function will be called at the time of execution
import sys
import os


""" Region for the welcome Screen and general function for the Registration Login and Admin"""
### General region for the function Welcome Screen Login and registration
def welcome_screen():
    print("######### Welcome User Please Enter the choice in the following Options ########")
    print("Choices : \n Register : R \n Login : L \n Admin login : A")
    user_choice = input()
    return user_choice
 
# Login Screen It just takes the vlaues from the user and passes to the function
def Login_screen():
    print("Please Enter the Username and Contact number for Login")
    username = input("Username :")
    try:
        contact_number = eval(input("Contact Number : "))
        # if  is integer( contact_number )
        #     print("Please Enter a valid number entering login screen: ")
        #     Login_screen()
    except:
        print(f'Error Occured {sys.exc_info()[0]} Please enter a valid contact detail')
        choice = input("Would like to continue ?? Y/N : ")
        if choice == "Y":
            Login_screen()
        else:
            print("Shutting down app")
            quit()
    return username, contact_number


# Making Register fuction : Takes the username and contact number from the user and passes to the controller
def register():
    print("Please Enter the Username and Contact Details to Register : ")
    username = input("Username : ")
    try: 
        contact_number  = eval(input("Contact Number : "))
    except:
        print(f'Error Occured {sys.exc_info()[0]} Please Enter the valid contact detail')
        choice = input("Continue Y/N : ")
        if choice =="Y":
            register()
        else:
            print("Closing the registration and getting to the  main Screen :")
            welcome_screen()


# Making the admin login page function  it gets the values from the user and sends to the controller
def admin():
    print("Welcome to the admin Login ")
    print("Please Enter the username and admin password : ")
    username = input("Username : ")
    password = input("please Enter the password : ")
    return username, password 



# Common Function to show the error and share messages from the controller
def common_message(message):
    print(message)



""" Region for the Admin page - getting the details from the database via controlle and showing it Here."""
# specific functions for the admin to get the users and number of books.
def admin_page(users , books):
    print("Welcome to the Admin Page")
    print(f"Total admins Registered Till Now are : {len(users)}")
    for list in users:
        print(f"Registered Admin User : Username  {list[0]} and password : {list[1]}")
    print(f"Total books in the library are : {len(books)}")
    for refbooks in books:
        print(f"Book Details as : {refbooks}")

