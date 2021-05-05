from .Trello import Trello


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

    def create_checkitem(self):
        # TODO:implement
        pass

    def delete_checkitem(self):
        # TODO:implement
        pass

    