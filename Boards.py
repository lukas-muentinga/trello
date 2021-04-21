""" Methods for manipulating boards based on https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-memberships-get """


from .Trello import Trello
from typing import Union


def get_board():
    # TODO: implement
    pass


def create_board():
    # TODO: implement
    pass


def delete_board():
    # TODO: implement
    pass


def get_board_field():
    # TODO: implement
    pass


def get_board_actions():
    # TODO: implement
    pass


def get_board_memberships():
    # TODO: implement
    pass


def get_board_members():
    # TODO: implement
    pass


def add_board_member():
    # TODO: implement
    pass


def remove_board_member():
    # TODO: implement
    pass


def update_board_member_membership():
    # TODO: implement
    pass


def email_invite_board_member():
    # TODO: implement
    pass


def get_board_lists(trello: Trello, 
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
    return trello.get(f'boards/{board_id}/lists', json=data).json()


def get_board_lists_filtered():
    # TODO: implement
    pass


def create_board_list():
    # TODO: implement
    pass


def get_board_card():
    # TODO: implement
    pass


def get_board_cards():
    # TODO: implement
    pass


def get_board_cards_filtered():
    # TODO: implement
    pass


def get_board_stars():
    # TODO: implement
    pass


def get_board_checklist():
    # TODO: implement
    pass


def get_board_custom_fields():
    # TODO: implement
    pass


def get_board_labels():
    # TODO: implement
    pass


def create_board_label():
    # TODO: implement
    pass


