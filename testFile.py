from Book import Book
def test_book_details():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"

from BookCollection import BookCollection

def test_get_books_by_author():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    print(bc.getBooksByAuthor("KING, Stephen"))

    expected_output = ("Title: Rage, Author: King, Stephen, Year: 1977\n"
                       "Title: The Shining, Author: King, Stephen, Year: 1977\n"
                       "Title: Cujo, Author: King, Stephen, Year: 1981")

    assert bc.getBooksByAuthor("KING, Stephen") == expected_output

def test_get_all_books_in_collection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    expected_output = ("Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
                       "Title: Rage, Author: King, Stephen, Year: 1977\n"
                       "Title: The Shining, Author: King, Stephen, Year: 1977\n"
                       "Title: Cujo, Author: King, Stephen, Year: 1981")

    assert bc.getAllBooksInCollection() == expected_output

def test_remove_author():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    bc.removeAuthor("king, stephen")

    assert bc.recursiveSearchTitle("Cujo", bc.head) == False
    assert bc.recursiveSearchTitle("The Shining", bc.head) == False
    assert bc.recursiveSearchTitle("Rage", bc.head) == False
    assert bc.recursiveSearchTitle("Ready Player One", bc.head) == True


def test_recursive_search_title():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False

test_book_details()
