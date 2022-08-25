from src.library import Library
from src.item_builder import ItemBuilder
from src.user_builder import UserBuilder


class NumbID:
    """
    Utility class to provide unique identifier.

    Methods defined here:
        new_id(...)
            Provide next unique identifier, starts at 1.

        reset_id(...)
            Reset unique identifier.
    """
    id_number = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    # note that these use the @staticmethod adornment since no instance
    # attributes are used.
    @staticmethod
    def new_id():
        NumbID.id_number += 1
        return NumbID.id_number

    @staticmethod
    def reset_id():
        NumbID.id_number = 0


def scenario_jonny_codewarrior():
    pass


def scenario_judy_hacker(library):
    """
    Judy Hacker, has fines of £2 outstanding,
    would like a DVD “Debugging to music”,
    does have a book out (not overdue) and is bringing back an overdue journal.
    """
    library.checkout_item(1, "New Moon", date=datetime.now() - timedelta(days=32))
    library.return_item(1, "New Moon")
    library.checkout_item(1, "Twilight")
    library.checkout_item(1, "Debugging to music")
    library.return_item(1, "Pirates of the Caribbean: The Journal")

def scenario_miss_marple():
    pass


def scenario_eric_halfbee(library):
    """
    Eric Halfbee comes in with a pile of overdue items,
    but doesn’t know if he has enough money to pay off his debts.
    If he has, he’d like a borrow a DVD.
    """
    library.checkout_item(3, "Life of Pi", date=datetime.now() - timedelta(days=40))
    library.checkout_item(3, "Labyrinth", date=datetime.now() - timedelta(days=40))
    library.checkout_item(3, "The Tales of Beedle the Bard", date=datetime.now() - timedelta(days=40))
    library.return_item(3, "Life of Pi")
    library.return_item(3, "Labyrinth")
    library.return_item(3, "The Tales of Beedle the Bard")
    fine = library.get_total_fine(3)
    print(f"Outstanding fine: £{fine:.2f}")
    library.pay_fine(3, 10)
    library.checkout_item(3, "Pirates of the Caribbean")


def build_library(library):
    item_builder = ItemBuilder()

    item_builder.set_library(library)

    item_builder.load_books_in_file("top100t.txt")
    item_builder.create_dvd("Pirates of the Caribbean")
    item_builder.create_journal("Pirates of the Caribbean: The Journal")

    item_builder.populate_library()


def build_users(library):
    user_builder = UserBuilder()
    user_builder.set_library(library)

    # TODO: Generate users from Enums instead of for loop
    for i in range(0, 4):
        user_builder.create_user()


if __name__ == '__main__':
    print("Welcome to Alexandria")

    lib_controller = Library(max_loans=5, max_fines=50)

    build_library(lib_controller)

    build_users(lib_controller)



