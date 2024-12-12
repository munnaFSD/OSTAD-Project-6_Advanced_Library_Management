from load_books import load_books

def view_books():
    all_books = load_books()

    if not all_books:
        print("\nError: 'No books available right now.'")
        return
    print("\nAll Book Lists")
    print("------------------")
    for index,book in enumerate(all_books, start=1):
        print(f"{index}. Title: {book['title']} || Author: {book['author']} ||  ISBN: {book['isbn']} || Year: {book['year']} || Price: ${book['price']} || Quantity: {book['quantity']} || BookAddedAt: {book['bookAddedAt']}")
    return
