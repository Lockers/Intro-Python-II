# Write a class to hold player information, e.g. what room they are in
# currently.

import random
from room import Room
from items import Item


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Hero(Person):
    def __init__(self, name, age, room, items=[]):
        super().__init__(name, age)
        self.room = room
        self.items = Item(items)

        def getStuff(item):
            self.items.append(item)

        def __str__(self):
            return f'{self.name}'
