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

    # HANDLERS

    def handle_help_choice(self, choice):
        self.display.help_menu()
        while choice != "4":
            self.display.help_item(int(choice))
            self.display.help_menu()
            choice = input("\n> ")
        self.main_menu()


    def handle_menu_choice(self, choice):
        if choice is "1":
            self.display.intro(self.player.location)
            self.player.name = input("\nPlease enter your name : ")
            self.display.infos(self.player, self.horde, self.day)
            #TODO
            return False
        elif choice is "2":
            self.display.help_menu()
            choice = input("\n> ")
            self.handle_help_choice(choice)
        else:
            exit("\n [Afraid ? I knew it.]")

    # /HANDLERS

    
    # MENUS

    def help_menu(self):
        self.display.help_menu()
        choice = input("\n> ")
        self.handle_help_choice(choice)


    def main_menu(self):
        self.display.title()
        self.display.main_menu()
        choice = input("\n> ")
        self.handle_menu_choice(choice)

    # /MENUS

    def __init__(self):
        self.horde = Horde()
        self.display = Display()
        self.player = Player()
        self.day = 1


    def main(self):
        """The beginning of everything."""
        self.main_menu()


if __name__ == "__main__":
    game = Main()
    game.main()

