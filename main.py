import commands_handler
import storage


def main():
    address_book = storage.load_data()
    print("Welcome to the assistant bot!")

    commands_handler.handle(address_book)

    storage.save_data(address_book)

if __name__ == "__main__":
    main()