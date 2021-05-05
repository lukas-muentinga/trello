""" Methods for list manipulation based on https://developer.atlassian.com/cloud/trello/rest/api-group-lists/#api-lists-id-get"""


from .Trello import Trello
from .Cards import Card
from typing import Union


class List:

    __id: str
    __name: str
    __trello: Trello

    def __init__(self, trello: Trello, definition: dict):
        """ List object for lists in Trello boards.

        Args:
            trello (Trello): Session to trello
            id (str): Id of the list
        """
        self.__trello = trello
        self.__id = definition['id']
        self.__name = definition['name']

    def name(self):
        return self.__name

    def id(self):
        return self.__id

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


    def get_card():
        # TODO: implement
        pass


    def create_card(self,
                    name: str = None,
                    description: str = None,
                    position: Union[str, int] = 'bottom',
                    due: str = None,
                    due_complete: bool = False,
                    member_ids: list = [],
                    label_ids: list = [],
                    url: str = None,
                    # file = None,
                    source_card_id: str = None,
                    keep_from_source_card: Union[str, list] = 'all',
                    # map_address: str = None,
                    # map_locationName: str = None,
                    # map_coordinates: str = None
                    ) -> Card:
        """ Creates a new card

        Args:
            trello (Trello): Session to Trello.
            list_id (str): Id of the list to which the card should be added to.
            name (str, optional): Name of the card. Defaults to None.
            description (str, optional): Card-Description. Defaults to None.
            position (Union[str, int], optional): Position in the list. Either 'top', 'bottom' or int. Defaults to 'bottom'.
            due (date, optional): Due date of the card. Defaults to None.
            due_complete (bool, optional): Completeion-status for the due date of the card. Defaults to False.
            member_ids (list, optional): Members of the card. Defaults to [].
            label_ids (list, optional): The ids of the card's labels. Defaults to [].
            url (str, optional): Url-field of the card. Defaults to None.
            source_card_id (str, optional): Card from which this card should be copied. Defaults to None.
            keep_from_source_card (Union[str, list], optional): Which values should be kept from source card. Either 'all' or list. Defaults to 'all'.

        Returns:
            Card: Card object for further usage
        """
        # TODO: implement parameters: fileSource, address, locationName, coordinates

        data = {
            'name': name,
            'idList': self.__id,
            'desc': description,
            'pos': position,
            'due': due,
            'dueComplete': due_complete,
            'idMembers': ','.join(member_ids),
            'idLabels': ','.join(label_ids),
            'urlSource': url,
            # 'fileSource': file,
            'idCardSource': source_card_id,
            'keepFromSouce': keep_from_source_card if keep_from_source_card is str else ','.join(keep_from_source_card),
            # 'address': map_address,
            # 'locationName': map_location_name,
            # 'coordinates': map_coordinates
        }
        card_def = self.__trello.post('cards', json=data).json()
        return Card(self.__trello, card_def)


# ######## STATIC METHODS


def get_list():
    # TODO: implement
    pass