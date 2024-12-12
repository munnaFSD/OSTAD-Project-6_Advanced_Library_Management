from load_books import load_books
from save_books import save_books
from datetime import datetime
def update_book():
    all_books = load_books()
    title = input("\nEnter the Title of the book to update: ").capitalize().strip()
    for book in all_books:
        if book["title"] == title:
            print("\nCurrent details:", book)

            new_title = input("\nEnter new title: ").strip().capitalize()
            new_author  = input("Enter new authors: ").strip()
            
            while True:
                try:
                    new_year = int(input("Enter New Publishing Year: "))
                    if new_year <0:
                        print("\nError>> publishing year can't be a negative number.")
                        return
                    break
                except ValueError:
                    print("\nError>> Invalid input. Please enter a valid integer.")

            while True:
                try:
                    new_price = float(input("Enter New Price: "))
                    if new_price <0:
                        print("\nError>> Price Must be Positive number.")
                        return
                    break
                except ValueError:
                    print("\nError>> Invalid input. Please enter a valid integer.")

            while True:
                try:
                    new_quantity = int(input("Enter New Quantity: "))
                    break
                except ValueError:
                    print("\nError>> Invalid input. Please enter a valid Price.")

            new_bookAddedAt = datetime.now().strftime("%d-%m-%Y-%H:%M-%S")

            book['title']  = new_title or book['title']
            book["author"] = new_author or book["author"]
            book["year"] = new_year or book["year"]
            book["price"] = new_price or book["price"]
            book['quantity'] = new_quantity or book['quantity']
            book['new_bookAddedAt'] = new_bookAddedAt

            save_books(all_books)
            print("\nBook updated successfully!")
            return
    print("\nBook not found. Please try again!")