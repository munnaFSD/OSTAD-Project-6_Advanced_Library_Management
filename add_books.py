from load_books import load_books
from save_books import save_books
import random
from datetime import datetime

def add_book():

    all_books = load_books()

    #Take the title, and author name from user
    title = input("\nEnter Book Title: ").strip().capitalize()
    author  = input("Enter Author Name: ").strip()
    

    while True:
        try:
            year = int(input("Enter Publishing Year Number: "))
            if year <0:
                print("\nError>> publishing year can't be a negative number.")
                return
            break
        except ValueError:
            print("\nError>> Invalid input. Please enter a valid integer.")

    while True:
        try:
            price = float(input("Enter Book Price: "))
            if price <0:
                print("\nError>> Price Must be Positive number.")
                return
            break
        except ValueError:
            print("\nError>> Invalid input. Please enter a valid integer.")

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("\nError>> Invalid input. Please enter a valid Price.")

    isbn = random.randint(100000, 999999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y-%H:%M-%S")

    contacts = {
        'title' : title,
        'author' : author,
        'year' : year,
        'isbn' : isbn,
        'price' : price,
        'quantity' : quantity,
        'bookAddedAt' : bookAddedAt
    }
    all_books.append(contacts)
    save_books(all_books)
    print("\n'Your Books added successfully!'")
    return
