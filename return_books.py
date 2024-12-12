from load_books import load_books, load_lend_data
from save_books import save_books, save_lend_data

def return_book():
    return_details = load_lend_data()
    all_books = load_books()
    title = input("\nEnter the Title of the book to return: ")
    phone = input("Enter the Phone of the book to return: ")
    for book in all_books:
        if (book["title"].lower() == title.lower()):
            for details in return_details:
                if (details['borrower_phone'] == phone):
                    book["quantity"] += 1

                    return_details.remove(details)
                    save_lend_data(return_details)

                    save_books(all_books)
                    print("\nBook returned successfully!")
                    return
                else:
                    print("\nInvalid phone or not found")
                    return
    print("\nError>> Book not found.")