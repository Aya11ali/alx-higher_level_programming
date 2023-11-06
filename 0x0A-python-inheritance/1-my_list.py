#!/usr/bin/python3
"""print a list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)

        Args:
            None

        Returns:
            None
        """
        my_list = sorted(self)
        if my_list:
            print(my_list)
