# Implement a class to hold room information. This should have name and
# description attributes.
from items import Item

class Room:
    def __init__(self, name, description, items = [], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = Item(items)

    def __str__(self):
        return f'Room: {self.name}, description: {self.description}'
