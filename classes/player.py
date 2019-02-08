#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class defining the player's values."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import random
import dictionaries

class Player:

    def __init__(self, name=dictionaries.names[random.randint(0,19)]):
        self.ammo = 2
        self.food = 2
        self.hp = 3
        self.name = name


    def choose_name():
        return 0
