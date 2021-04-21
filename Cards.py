""" Methods for manipulating cards based on https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post """

from .Trello import Trello
from datetime import date

from typing import Union

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
                ) -> dict:
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
        TODO
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
    return trello.post('cards', json=data).json()


def get_card():
    # TODO: implement
    pass


def update_card():
    # TODO: implement
    pass


def delete_card():
    # TODO: implement
    pass


def get_card_field():
    # TODO: implement
    pass


def get_card_action():
    # TODO: implement
    pass


def get_card_attachments():
    # TODO: implement
    pass


def delete_card_attachment():
    # TODO: implement
    pass


def get_card_board():
    # TODO: implement
    pass


def get_card_checklist_items():
    # TODO: implement
    pass


def update_card_checklist_item():
    # TODO: implement
    pass


def get_card_checklists():
    # TODO: implement
    pass


def create_card_checklist():
    # TODO: implement
    pass


def delete_card_checklist():
    # TODO: implement
    pass


def create_card_checkitem():
    # TODO: implement
    pass


def update_card_checkitem():
    # TODO: implement
    pass


def delete_card_checkitem():
    # TODO: implement
    pass


def get_card_list():
    # TODO: implement
    pass


def get_card_members():
    # TODO: implement
    pass


def add_card_member():
    # TODO: implement
    pass


def remove_card_member():
    # TODO: implement
    pass


def get_card_voters():
    # TODO: implement
    pass


def add_card_member_vote():
    # TODO: implement
    pass


def remove_card_member_vote():
    # TODO: implement
    pass


def get_card_plugin_data():
    # TODO: implement
    pass


def get_card_stickers():
    # TODO: implement
    pass


def update_card_sticker():
    # TODO: implement
    pass


def add_card_comment():
    # TODO: implement
    pass


def delete_card_sticker():
    # TODO: implement
    pass


def add_card_comment():
    # TODO: implement
    pass


def update_card_comment():
    # TODO: implement
    pass


def delete_card_comment():
    # TODO: implement
    pass


def get_card_custom_field():
    # TODO: implement
    pass


def update_card_custom_field():
    # TODO: implement
    pass


def add_card_label():
    # TODO: implement
    pass


def create_card_label():
    # TODO: implement
    pass


def remove_card_label():
    # TODO: implement
    pass


def mark_card_notification_read():
    # TODO: implement
    pass


