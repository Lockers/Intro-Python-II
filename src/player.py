# Write a class to hold player information, e.g. what room they are in
# currently.

import random

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Hero(Person):
    def __init__(self, name, height, age, speciality, health, items=[]):
        super().__init__(name, height, age)
        self.speciality = speciality
        self.health = health
        self.items = items

        def attack(self):
            damage = random.randint(1, 21) * items[0] # << To do multiplier based on weapon items
            return damage


class Monster(Person):
    def __init__(self, name, height, age, danger, health, armour):
        super().__init__(name, height, age)
        self.danger = danger
        self.health = health
        self.armour = armour

        def attack(self):
            damage = random.randint(1, 21) * danger # << To do multiplier based on danger
            return damage