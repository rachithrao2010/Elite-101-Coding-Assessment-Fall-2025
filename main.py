from datetime import timedelta, date, datetime
from library_books import library_books

# Hello, Grader. This comment is for you. I have been learning java for a while and have just recently learnt about javadoc comments.
# I think they are really handy. Since you will be testing our functions directly, i thought they might come in handy for you as well.
# Allow me to present "Pythondoc" comments, which follow the same structure. An example is:
'''
# (description of functions purpose)
# return values
# parameters
'''
# I will be omitting preconditions and postconditions in these.

class book:
    '''
    # this fucntion initializes the book object. it takes every parameter included in the input dictionary.
    # does not return anything
    # parameters are id, title, author, genre, avaliable, due_date, checkouts. These are not provided by the user, but are automatically added by parsing the input file.
    '''
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    '''
    # checks out a book
    # does not return anything
    # takes no input, but does use self values.
    '''
    def checkout(self):
        if self.available == True:
            self.checkouts += 1
            self.available = False 
            self.due_date = date.today() + timedelta(weeks=2)
        else:
            print("Sorry, This book is not available right now.")
    
    '''
    # returns a book
    # does not return anything
    # takes no input, but does use self values.
    '''
    def return_book(self):
        self.available = True
        self.due_date = None

books = []



'''
# converts given list of dictionaries to list of  objects using class book
# does not return anything
# input is handled internally
'''
def convert_dict():
    for item in library_books:
        books.append(book(item["id"], item["title"], item["author"], item["genre"], item["available"], item["due_date"], item["checkouts"]))



'''
# iterates throuhg list of books and prints out available ones.
# does not return anything
# does not use input
'''
def view_books():
    print("ID" + (" " * 10) + "Title" + (" " * 50) + "Author \n \n")
    
    for item in books:
        if item.available == True:
            id = item.id
            title = item.title
            author = item.author

            print(id + (" " * (12 - len(id))) + title + (" " * (55 - len(title))) + author)
            print()



'''
# searches by Genre or Author
# does not return anything
# input is handled internally
'''
def search():
    printed_output = False
    search = input("Please Enter a Keyword that matches either the Book's Author or Genre:   ")
    search = search.capitalize()
    print("ID" + (" " * 10) + "Title" + (" " * 50) + "Author \n \n")
    for item in books:
        if item.author == search or item.genre == search:
            id = item.id
            title = item.title
            author = item.author
            printed_output = True
            print(id + (" " * (12 - len(id))) + title + (" " * (55 - len(title))) + author)
            print()
    if printed_output == False:
        print("We couldn't find any matches, Please Try Again.")



'''
# checks out a book using class book's mehod checkout()
# does not return anything
# input is handled internally
'''
def checkout_book():
    ID = input("Please Enter A book ID:   ")
    for item in books:
        if item.id == ID:
            chosen_book = item
    
    if chosen_book.available == True:
        chosen_book.checkout()
        print(f'You have Successfully checked out {chosen_book.title}. It is due on {chosen_book.due_date}.')
    elif chosen_book.available == False:
        print("Sorry, This book is not Available")



'''
# returns a book using class book's method return_book()
# does not return anything
# input is handled internally
'''
def Return_book():
    ID = input("Please Enter A book ID:   ")
    for item in books:
        if item.id == ID:
            chosen_book = item
    
    if chosen_book.available == False:
        chosen_book.return_book()
        print(f'You have Successfully returned {chosen_book.title}.')
    elif chosen_book.available == True:
        print("This Book is currently Available")



'''
# lists overdue books.
# does not return anything
# input is handled internally
'''
def view_overdue():
    printed_output = False
    print("ID" + (" " * 10) + "Title" + (" " * 50) + "Author \n \n")
    for item in books:
        if item.due_date != None:
            book_due_date = datetime.strptime(item.due_date, r"%Y-%m-%d").date()
            if date.today() > book_due_date and item.available == False:
                id = item.id
                title = item.title
                author = item.author
                printed_output = True
                print(id + (" " * (12 - len(id))) + title + (" " * (55 - len(title))) + author)
                print()
    if printed_output == False:
        print("Good News! There are no Overdue Books!")




convert_dict()

menu_options = ["View Books - [1]", "Check out a book - [2]", "Return a book - [3]", "Search by ID or Author - [4]", "View Overdue books - [5]"]
print("Welcome To the Library!")
for item in menu_options:
    print(item)
    print()
option = input("please type a number from 1 to 5:   ")
while int(option) not in [1, 2, 3, 4, 5]:
    option = input("That wasn't a valid option. Please type a number from 1 to 5:   ")

if option == "1":
    view_books()
if option == "2":
    checkout_book()
if option == "3":
    Return_book()
if option == "4":
    search()
if option == "5":
    view_overdue()
    