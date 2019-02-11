#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Zombie-Survival.py: Survive zombies in a roguelike text-based game"""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"


from classes.horde import Horde
from classes.player import Player
from classes.display import Display
import constants
import dictionaries

class Main:


    def __init__(self):
        self.horde = Horde()
        self.display = Display()
        self.player = Player()


    def main(self):
        """The beginning of everything."""
        self.display.title()
        self.display.intro(self.player.location)


if __name__ == "__main__":
    game = Main()
    game.main()

