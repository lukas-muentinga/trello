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
        self.__trello = Trello

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

        result = self.__trello.post(f'boards/{self.__id}/lists')
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


######## STATIC METHODS #################################################


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
              background: str = 'grey',
              card_aging_type: str = 'regular') -> Board:

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
        background (str, optional): Background of the board. Defaults to 'grey'.
            Valid values: bule, orange, green, red, purple, pink, lime, sky, grey.
        card_aging_type (str, optional): Type of card aging. Defaults to 'regular'.
            Valid values: regular, pirate.

    Returns:
        Board: Board object for further usage
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

    json = {k: v for k, v in json.items() if v is not None}

    board_values = trello.post('boards', json=json).json()
    return Board(trello, board_values['id'])