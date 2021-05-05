from requests import Session
from requests_oauthlib import OAuth1

from . import config
from .Boards import Board

url = 'https://api.trello.com/1/'


class Trello (Session):
    """TODO: Docstring"""

    def __init__(self):
        super().__init__()
        self.auth = OAuth1(client_key=config.APP_KEY, resource_owner_key=config.API_TOKEN)

    def get(self, path, json=None, data=None):
        # TODO: doku
        return super().get(f'{url}/{path}', json=json, data=data)

    def post(self, path, data=None, json=None):
        # TODO: doku
        return super().post(f'{url}/{path}', data=data, json=json)

    def patch(self, url, data=None, json=None):
        # TODO: implement
        super().patch(url, data=data, json=json)

    def delete(self, url):
        # TODO: implement
        super().delete(url)

    def create_board(self,
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

        board_values = self.post('boards', json=json).json()
        return Board(self, board_values['id'])

    def get_board():
        # TODO: implement
        pass
