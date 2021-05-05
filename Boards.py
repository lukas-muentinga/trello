""" Methods for manipulating boards based on https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-memberships-get """


from .Trello import Trello
from .Lists import List
from typing import Union


class Board:

    __id: str
    __trello: Trello

    def __init__(self, trello: Trello, id: str):
        """ Board object representing Trello boards

        Args:
            trello (Trello): Session to Trello
            id (str): Id of the board
        """
        self.__id = id
        self.__trello = trello

    def delete():
        # TODO: implement
        pass

    def get_fields():
        # TODO: implement
        pass

    def get_actions():
        # TODO: implement
        pass

    def get_memberships():
        # TODO: implement
        pass

    def get_members():
        # TODO: implement
        pass

    def add_member():
        # TODO: implement
        pass

    def remove_member():
        # TODO: implement
        pass

    def update_member_membership():
        # TODO: implement
        pass

    def email_invite_member():
        # TODO: implement
        pass

    def get_lists(self,
                  board_id: str,
                  cards: str = None,
                  card_fields: Union[str, list] = 'all',
                  filter: str = 'all',
                  fields: Union[str, list] = 'all') -> dict:
        """ Gets all lists from a board

        Args:
            trello (Trello): Session to trello
            board_id (str): board-id
            cards (str, optional): Filter for cards. Either 'all', 'closed', 'none' or 'open'. Defaults to None.
            card_fields (Union[str, list], optional): Which card fields to return. Either 'all' or list. Defaults to 'all'.
            filter (str, optional): Filter for lists. Either 'all', 'closed', 'none' or 'open'. Defaults to 'all'.
            fields (Union[str, list], optional): [description]. Defaults to 'all'.

        Returns:
            dict: [description] TODO
        """
        data = {
            'cards': cards,
            'card_fields': card_fields,
            'filter': filter,
            'fields': fields
        }
        return self.__trello.get(f'boards/{board_id}/lists', json=data).json()

    def get_lists_filtered():
        # TODO: implement
        pass

    def create_list(self,
                    name: str,
                    position: Union[str, int] = 'bottom') -> List:
        """ Creates a new list on the board

        Args:
            name (str): Name of the list
            position (Union[str, int], optional): Position of the list. Either 'top', 'bottom' or int. Defaults to 'bottom'.

        Returns:
            List: List object for further usage
        """

        json = {
            'id': self.__id,
            'name': name,
            'pos': position
        }

        result = self.__trello.post(f'boards/{self.__id}/lists', json=json).json()
        return List(self.__trello, result)

    def get_card():
        # TODO: implement
        pass

    def get_cards():
        # TODO: implement
        pass

    def get_cards_filtered():
        # TODO: implement
        pass

    def get_stars():
        # TODO: implement
        pass

    def get_checklist():
        # TODO: implement
        pass

    def get_custom_fields():
        # TODO: implement
        pass

    def get_labels():
        # TODO: implement
        pass

    def create_label():
        # TODO: implement
        pass
