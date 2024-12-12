from add_books import add_book
from view_books import view_books
from update_books import update_book
from delete_books import delete_book
from lend_books import lend_book
from return_books import return_book

def menu_options():
    print(
        "\n\n---------------------------------------------"
        "\nWelcome to the Contact Book Management System",
        "\n---------------------------------------------"
    )
    options = [
        "Add New Book",
        "View All Books",
        "Update Book",
        "Remove Book",
        "Lend Book",
        "Return Book",
        "Exit the Program"
    ]
    for index, each_option in enumerate(options, start=1):
        print(f"{index}. {each_option}")
    return True


def main():

    while True:
        menu_options()

        choice = input("\nEnter your choice number(1/7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            lend_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("\n'Thank you for choosing our Book management system!'\n")
            break
        else:
            print("\nError>> Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
