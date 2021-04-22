""" Methods for manipulating boards based on https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-memberships-get """


from .Trello import Trello
from typing import Union


def get_board():
    # TODO: implement
    pass

def create_board(trello: Trello,
              name: str,
              use_default_labels: bool = True,
              use_default_lists: bool = True,
              description: str = None,
              organization_id: str = None,
              source_board_id: str = None,
              keep_cards_from_source: bool = False,
              power_ups: str = None,
              permission_lvl: str = 'private',
              voting_rights: str = 'disabled',
              comment_rights: str = 'members',
              invitation_rights: str = 'members',
              allow_self_join: bool = True,
              enable_card_covers: bool = True,
              background: str = 'sky',
              card_aging_type: str = 'regular') -> dict:

    """Creates a new Trello-board

    Args:
        trello (Trello): Session to trello.
        name (str): Name of the board. 1-16384 chars long.
        use_default_labels (bool, optional): Defines whether board should be created with the default label set. Defaults to True.
        use_default_lists (bool, optional): Defines whether board should be created with the default lists (To Do, Doing, Done). 
            Defaults to True.
        description (str, optional): Board-description. Defaults to None.
        organization_id (str, optional): Id of the organization the board should belong to. Defaults to None.
        source_board_id (str, optional): Id of the board from which the new one should be copied. Defaults to None.
        keep_cards_from_source (bool, optional): Whether the cards from the source board should be copied. Defaults to False.
        power_ups (str, optional): Power-Ups that should be activated on this board. Defaults to None.
            Valid values: all, calendar, cardAging, recap, voting
        permission_lvl (str, optional): Permission level of the board. org, private or public. Defaults to 'private'.
        voting_rights (str, optional): Who is allowed to vote on the board. Defaults to 'disabled'.
            Valid values: disabled, members, observers, org, public.
        comment_rights (str, optional): Who can comment on the board. Defaults to 'members'.
            Valid values: disabled, members, observers, org, public.
        invitation_rights (str, optional): Who can invite new members. Defaults to 'members'.
            Valid values: members, admins.
        allow_self_join (bool, optional): Whether members can join the board themselves or have to be invited. Defaults to True.
        enable_card_covers (bool, optional): Whether card covers are enabled. Defaults to True.
        background (str, optional): Background of the board. Defaults to 'sky'.
            Valid values: bule, orange, green, red, purple, pink, lime, sky, grey.
        card_aging_type (str, optional): Type of card aging. Defaults to 'regular'.
            Valid values: regular, pirate.
    """

    json = {
        'name': name,
        'defaultLabels': use_default_labels,
        'defaultLists': use_default_lists,
        'desc': description,
        'idOrganization': organization_id,
        'idBoardSource': source_board_id,
        'keepFromSource': 'cards' if keep_cards_from_source else None,
        'powerUps': power_ups,
        'prefs_permissionLevel': permission_lvl,
        'prefs_voting': voting_rights,
        'prefs_comments': comment_rights,
        'prefs_invitations': invitation_rights,
        'prefs_selfJoin': allow_self_join,
        'prefs_cardCovers': enable_card_covers,
        'prefs_background': background,
        'prefs_cardAging': card_aging_type
    }

    json = {v for k, v in json.items() if v is not None}

    return trello.post('boards', data=json).json()


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


