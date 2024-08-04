import pickle

from address_book.address_book import AddressBook


def save_data(book, filename="data/addressbook.pkl"):
    """stora data into file"""

    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="data/addressbook.pkl"):
    """load data from file"""

    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()