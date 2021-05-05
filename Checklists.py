from .Trello import Trello
from typing import Union


class Checklist():
    __id: str
    __trello: Trello

    def __init__(self, trello: Trello, definition: dict):
        self.__id = definition['id']
        self.__trello = trello

    def update(self):
        # TODO:implement
        pass

    def delete(self):
        # TODO:implement
        pass

    def get_field(self):
        # TODO:implement
        pass

    def update_field(self):
        # TODO:implement
        pass

    def get_board(self):
        # TODO:implement
        pass

    def get_card(self):
        # TODO:implement
        pass

    def get_checkitem(self):
        # TODO:implement
        pass

    def create_checkitem(self,
                         name: str,
                         position: Union(str, int) = 'bottom',
                         is_checked: bool = False):
        """Creates a checklist item on the checklist

        Args:
            name (str): Title of the checklist item
            position (str or int, optional): Position in the checklist. Either 'top', 'bottom' or int.
                Defaults to 'bottom'.
            is_checked (bool, optional): Whether the checklist item should be checked. Defaults to False.
        """
        data = {
            'name': name,
            'pos': position,
            'checked': is_checked,
        }
        self.__trello.post(f'checklists/{self.__id}/checkItem', json=data)

    def delete_checkitem(self):
        # TODO:implement
        pass

    