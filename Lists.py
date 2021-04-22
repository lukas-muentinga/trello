""" Methods for list manipulation based on https://developer.atlassian.com/cloud/trello/rest/api-group-lists/#api-lists-id-get"""


from .Trello import Trello
from typing import Union


class List:

    __id: str
    __trello: Trello

    def __init__(self, trello: Trello, id: str):
        """ List object for lists in Trello boards.

        Args:
            trello (Trello): Session to trello
            id (str): Id of the list
        """

    def update():
        # TODO: implement
        pass

    def archive():
        # TODO: implement
        pass

    def move_to_board():
        # TODO: implement
        pass

    def unarchive():
        # TODO: implement
        pass

    def archive_all_cards():
        # TODO: implement
        pass

    def move_all_cards():
        # TODO: implement
        pass

    def update_field():
        # TODO: implement
        pass

    def get_actions():
        # TODO: implement
        pass

    def get_board():
        # TODO: implement
        pass

    def get_cards():
        # TODO: implement
        pass


def get_list():
    # TODO: implement
    pass