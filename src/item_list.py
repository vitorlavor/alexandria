# Libraries
from item import Item
from user import UserClass


class ItemList:

    def __init__(self):
        # initialise instance attributes
        self._list = list()
        pass

    def __del__(self):
        # initialise instance attributes
        pass

    # @staticmethod

    def add_item(self, item):
        """ Adds an item to the list

        :param item:
        """
        self._list.append(item)

    def get_item_from_title(self, identifier):
        """ Checks if an item is in the list based on its Title

        :param identifier: Title
        :return: item
        """
        for item in self._list:
            item_identifier = item.get_title(identifier)
            if identifier == item_identifier:
                return item

    def get_item_from_id(self, identifier):
        """ Checks if an item is in the list based on its ID

        :param identifier: ID
        :return: item
        """
        for item in self._list:
            item_identifier = item.get_id(identifier)
            if identifier == item_identifier:
                return item

    def number_of_items(self):
        """ Gets the number of items in the list

        :return: Number of items in the list
        """
        return len(self._list)

    def get_fines(self, item):
        """ Calculates the fine of an item

        :param item:
        :return: Fine for the item
        """
        return item.get_fine_due()

    def get_total_fines(self):
        """ Calculates the total amount of fines of overdue items

        Return: Fine for all
        :return:
        """
        fines = 0
        for item in self._list:
            fines += item.get_fine_due()
        return fines

    def checkout_item(self, item):
        """ Adds an item to the list and set the checkout date

        :return:
        """
        self._list.append(item)
        item.set_checkout()

    def return_item(self, item):
        """ Removes an item to the list and reset the checkout date

        :return:
        """
        self._list.remove(item)
        item.reset_checkout()

if __name__ == '__main__':
    pass