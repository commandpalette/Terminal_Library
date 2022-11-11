from tkinter import *
import pubsub as pub
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
import tkintertable as tktable
from tkintertable import Tables
import datetime

#self.table.insert('', 'end', text="1", values=(book))


class Dashboard():
    
    ### Parts that are inclded are __init__
    

    def __init__(self , username , bookcount , *book_details) -> None:
        self.dashboard = Tk()
        self.dashboard.title("Library - Manager")
        self.dashboard.geometry('950x600')
        self.username = username
        self.bookcount = bookcount
        self.raw_details = []
        self.taken_books = []
        self.books_to_take = []
        self.whole_book = []
        self.book_details  = book_details
        

    def populating_book_list(self):
        ## Defining the book list to take and  taken already
        self.taken_books  = []
        self.to_take_books = []
        self.whole_book = []
        ## Populating the book list
        self.taken_books = self.book_details[0]
        self.to_take_books = self.book_details[1]
        self.whole_book = self.book_details[2]
        

    def defining_static_controls(self):
        # Frames for dashboard
        self.upper_layout  = Frame(self.dashboard )
        self.main_layout = Frame(self.dashboard)
        self.bottom_layout = Frame(self.dashboard)

        # Controls for the dashboard
        self.amount_label  = Label(self.upper_layout , text="Amount Incured || 0 ")
        self.username_label = Label(self.upper_layout , text="Welcome || " + self.username) 
        self.books_label = Label(self.upper_layout , text="Books Taken || " + str(self.bookcount))


    # Here the working Functions to work
    def inserting_data_into_table(self):
        #self.table.insert('' , 'end' , text="1" ,values = ("Book Name" , "Book Publication" , "Book Author" , "Rented date"))
        for books in self.whole_book:
            self.table.insert('' ,'end' , text="1" , values=(books[0] , books[1] , books[2] , books[3]))

    # def rent_book_click(self):
    #     today_date = datetime.date.today()
    #     # datetime.strptim(date1 , "%Y/%M/%D")
    #     value  = self.datepicker.get()
    #     temp  = datetime.datetime(value)




    def defining_dynamic_controls(self):
        # Calling function to populate the book list
        self.populating_book_list()
        var_choose = StringVar()
        var_return = StringVar()
        var_choose.set("Available Books")
        var_return.set("Choose to return")

        # Setting the options menu and the date picker to choose the book to rent
        self.books = OptionMenu(self.main_layout , var_choose, *self.to_take_books)
        #self.datepicker = DateEntry(self.main_layout)
        self.rentbook = Button(self.main_layout ,text="Rent Selected Book" )

        self.rented_books = OptionMenu(self.main_layout , var_return ,  *self.taken_books)
        self.delete_book = Button(self.main_layout , text="Return Rented Book")

        # Bottom table controls which will be updated time to time
        self.table  = ttk.Treeview(self.bottom_layout,  columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
        self.table.column("# 1" , anchor=CENTER)
        self.table.heading("# 1", text="Book Name")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor=CENTER)
        self.table.heading("# 4", text="Rented Date")
        self.table.column("# 5" , anchor=CENTER)
        self.table.heading("# 5", text="Rent Charged")

    def placing_controls(self):
        # Placement for the static controls
        self.upper_layout.pack(fill=BOTH , pady=12)
        self.main_layout.pack(fill=BOTH , pady=12)
        self.books_label.pack(side=LEFT , padx=15)
        self.amount_label.pack(side=LEFT, padx=15)
        self.username_label.pack(side=RIGHT , padx=10)

        # Placement for the dynamic controls
        self.books.pack(side=LEFT , padx=5)
        #self.datepicker.pack(side=LEFT , padx=5)
        self.rentbook.pack(side=LEFT , padx=5)

        self.delete_book.pack(side=RIGHT , padx=5 , )
        self.rented_books.pack(side=RIGHT , padx=5)

        self.bottom_layout.pack(fill=BOTH, expand=True , side=TOP)
        self.table.pack(side=TOP, fill="both", expand=True)

        # Calling the inserting fuction
        self.inserting_data_into_table()

        self.dashboard.mainloop()
        



if __name__ == '__main__':
    name  = Dashboard()
    name.defining_static_controls()
    name.placing_controls()