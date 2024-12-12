import json

BOOKS_FILE = 'books_store.json'
LEND_FILE = 'lend_books.json'

def save_books(store_books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(store_books, file, indent=4)
        return


def save_lend_data(lend_books):
    with open(LEND_FILE, 'w') as file:
        json.dump(lend_books, file, indent=4)
        return