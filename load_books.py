import json,os

BOOKS_FILE = 'books_store.json'
LEND_FILE = 'lend_books.json'

def load_books():
    try:
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(e)
        return []


def load_lend_data():
    try:
        if os.path.exists(LEND_FILE):
            with open(LEND_FILE, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(e)
        return []