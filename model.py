# Place to import diff modules 
import mysql.connector


""" Database Connection """
# Connect with the MySQL database 
mydb = mysql.connector.connect(host="localhost" , user="root" , passwd="vinay")
db = mydb.cursor()
""" The tables for the users and books with the relevant columns already been made """

# Class defined for the books and will be used to save the data in the database.
class books():
    def __init__(self ,author , name , company) -> None:
        self.author = author
        self.name = name
        self.company = company

    def update(self, date , user):
        self.date = date
        self.user = user
    
    def show(self):
        return self.author, self.name , self.company , self.date , self.user

# Search for the admin and lets the user enter the app as admin
def search_admin(username , password):
    db.execute("USE terminal_library;")
    sql = "SELECT * FROM admins WHERE username = (%s) AND pasword = (%s);"
    values = (username, password)
    db.execute(sql,values)
    list = db.fetchall()
    if len(list) > 0 :
        return True
    else:
        return False


# used to fetch the data for the admin page
def admin_details():
    db.execute("USE terminal_library;")
    db.execute("SELECT * FROM admins;")
    adminlist = db.fetchall()
    db.execute("SELECT * FROM books")
    booklist = db.fetchall()
    return adminlist, booklist

"""Checking the user and if exists already then registering them into the database"""
def check_and_register_user(username, contact_details):
    db.execute("USE terminal_library;")
    sql = "SELECT * FROM users WHERE username = (%s) AND contact = (%s);"
    values = (username, contact_details)
    db.execute(sql,values)
    list = db.fetchall()
    for lines in list:
        if contact_details == lines[1]:
            return False
        else:        
            under_sql = "INSERT INTO users (user_name, contact) VALUES ((%s) , (%s));"
            values = username , contact_details
            values = (username, contact_details)
            db.execute(under_sql , values)
            return True

def check_and_login_user(username, contact_details):
    db.execute("USE terminal_library;")
    sql = "SELECT * FROM users WHERE username = (%s) AND contact = (%s);"
    values = (username, contact_details)
    db.execute(sql,values)
    list = db.fetchall()
    for lines in list:
        if contact_details == lines[1]:
            return True
        else:        
            return False