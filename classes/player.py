#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class defining the player's values."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import random
import dictionaries
import constants

class Player:


    def get_random_location(self):
        adjective = dictionaries.adjectives[random.randint(0, len(dictionaries.adjectives) - 1)]
        place = dictionaries.places[random.randint(0, len(dictionaries.places) - 1)]

        return adjective + " " + place


    def get_random_state(self):
        state = dictionaries.states[random.randint(0, len(dictionaries.states) - 1)]

        return state


    def __init__(self, name=dictionaries.names[random.randint(0,19)]):
        self.ammo = constants.AMMO_START
        self.food = constants.FOOD_START
        self.name = name
        self.location = self.get_random_location()
        self.state = self.get_random_state()


    def choose_name():
        return 0
