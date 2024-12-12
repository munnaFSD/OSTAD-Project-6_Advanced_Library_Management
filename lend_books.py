from load_books import load_books, load_lend_data
from save_books import save_lend_data, save_books
from datetime import datetime,timedelta
def lend_book():

    all_books = load_books()
    lend_data = load_lend_data()

    title = input("\nEnter the book title to lend: ").strip().capitalize()

    for book in all_books:
        if book['title'].lower() == title.lower():
            if book['quantity'] <= 0:
                print("\nThere are not enough books available to lend.")
                return
            
            borrower_name = input("Enter the borrower's name: ").strip().capitalize()
            borrower_phone = input("Enter the borrower's phone number: ").strip()
            if borrower_phone.isdigit()  and borrower_phone[:2] == '01' :
                due_date = datetime.now() + timedelta(days=7)
            else:
                print("\nError>> Invalid Phone! Please type valid Number.")
                return

            lend_info = {
                'title': book['title'],
                'borrower_name': borrower_name,
                'borrower_phone': borrower_phone,
                'due_date': due_date.strftime('%Y-%m-%d')
            }

            lend_data.append(lend_info)
            book['quantity'] -= 1
            save_lend_data(lend_data)

            save_books(all_books)

            print(f"\nBook lent successfully! Return due by {due_date.strftime('%Y-%m-%d')}.")
            return

    print("\nError>> Book not found.")

