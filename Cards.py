""" Methods for manipulating cards based on https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post """

from .Trello import Trello
from datetime import date

from typing import Union


class Card:

    __trello: Trello
    __id: str

    def __init__(self, trello: Trello, def: dict):
        self.__trello = trello
        self.__id = def['id']

    def update():
        # TODO: implement
        pass

    def delete():
        # TODO: implement
        pass

    def get_field():
        # TODO: implement
        pass

    def get_action():
        # TODO: implement
        pass

    def get_attachments():
        # TODO: implement
        pass

    def delete_attachment():
        # TODO: implement
        pass

    def get_board():
        # TODO: implement
        pass

    def get_checklist_items():
        # TODO: implement
        pass

    def update_checklist_item():
        # TODO: implement
        pass

    def get_hecklists():
        # TODO: implement
        pass

    def create_checklist():
        # TODO: implement
        pass

    def delete_checklist():
        # TODO: implement
        pass

    def create_checkitem():
        # TODO: implement
        pass

    def update_checkitem():
        # TODO: implement
        pass

    def delete_checkitem():
        # TODO: implement
        pass

    def get_list():
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

    def get_voters():
        # TODO: implement
        pass

    def add_member_vote():
        # TODO: implement
        pass

    def remove_member_vote():
        # TODO: implement
        pass

    def get_plugin_data():
        # TODO: implement
        pass

    def get_stickers():
        # TODO: implement
        pass

    def update_sticker():
        # TODO: implement
        pass

    def delete_sticker():
        # TODO: implement
        pass

    def add_comment():
        # TODO: implement
        pass

    def update_comment():
        # TODO: implement
        pass

    def delete_comment():
        # TODO: implement
        pass

    def get_custom_field():
        # TODO: implement
        pass

    def update_custom_field():
        # TODO: implement
        pass

    def add_label():
        # TODO: implement
        pass

    def create_label():
        # TODO: implement
        pass

    def remove_label():
        # TODO: implement
        pass

    def mark_notification_read():
        # TODO: implement
        pass


######## STATIC METHODS #################


def get_card():
    # TODO: implement
    pass


def create_card(trello: Trello, 
                list_id: str,
                name: str = None,
                description: str = None,
                position: Union[str, int] = 'bottom',
                due: date = None,
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
        'idList': list_id,
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
    card_def = trello.post('cards', json=data).json()
    return Card(trello, card_def)
