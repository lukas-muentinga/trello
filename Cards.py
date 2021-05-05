""" Methods for manipulating cards based on https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post """

from .Trello import Trello
from .Checklists import Checklist
from datetime import date

from typing import Union


class Card:

    __trello: Trello
    __id: str

    def __init__(self, trello: Trello, definition: dict):
        self.__trello = trello
        self.__id = definition['id']

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

    def get_checklists():
        # TODO: implement
        pass

    def create_checklist(self,
                         name: str,
                         source_checklist_id: str = None,
                         position: Union(str, int) = 'bottom') -> Checklist:
        """ Creates a new checklist on the card

        Args:
            name (str): Name of the checklist
            source_checklist_id (str, optional): id of a checklist to copy from. Defaults to None.
            position (str or int, optional): Position of the checklist. Either 'top', 'bottom' or int.
                Defaults to 'bottom'.

        Returns:
            Checklist: Checklist object.
        """
        data = {
            'name': name,
            'idChecklistSource': source_checklist_id,
            'pos': position,
        }
        checklist_def = self.__trello.post(f'cards/{self.__id}/checklists', json=data).json()
        return Checklist(self.__trello, checklist_def)

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
