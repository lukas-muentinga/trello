""" Methods for manipulating cards based on https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post """

from .Trello import Trello
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
