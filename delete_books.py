from load_books import load_books
from save_books import save_books
def delete_book():
    all_books = load_books()
    isbn = int(input("\nEnter the ISBN of the book to delete: "))
    for book in all_books:
        if book["isbn"] == isbn:
            all_books.remove(book)
            save_books(all_books)
            print("\nBook deleted successfully!")
            return


    #books = [book for book in books if book["isbn"] != isbn]
    


    
