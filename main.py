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
import helpers
import actions

class Main:

    # HANDLERS

    def handle_help_choice(self, choice):
        self.display.help_menu()
        while choice != 4:
            self.display.help_item(int(choice))
            self.display.help_menu()
            choice = input("\n> ")
        if self.in_game:
            self.actions()
        else:
            self.main_menu()


    def handle_menu_choice(self, choice):
        if choice is 1:
            self.display.intro(self.player.location)
            self.player.choose_name()
            self.adventure()
            return False
        elif choice is 2:
            self.display.help_menu()
            choice = helpers.check_choice(4)
            self.handle_help_choice(choice)
        elif choice is 3:
            exit("\n [Afraid ? I knew it.]")


    def handle_actions_choice(self, choice):
        if choice is 3:
            self.help_menu()

        if self.am:
            if choice is 1:
                actions.scavenge()
            if choice is 2:
                actions.shoot()
        else:
            if choice is 1:
                actions.move()
            if choice is 2:
                actions.stay()

    # /HANDLERS

    
    # MENUS

    def help_menu(self):
        self.display.help_menu()
        choice = helpers.check_choice(4)
        self.handle_help_choice(choice)


    def main_menu(self):
        self.display.title()
        self.display.main_menu()
        choice = helpers.check_choice(3)
        self.handle_menu_choice(choice)


    def actions(self):
        if self.am:
            self.display.actions_day()
            choice_day = helpers.check_choice(3)
            self.handle_actions_choice(choice_day)
            self.am = False
            self.day+=1
        else:
            self.display.actions_night()

    # /MENUS


    def adventure(self):
        self.in_game = True
        while not helpers.check_end(self.day, self.player, self.horde):
            self.display.infos(self.player, self.horde, self.day, self.am)
            self.actions()
        else:
            print("the end")


    def __init__(self):
        self.in_game = False
        self.horde = Horde()
        self.display = Display()
        self.player = Player()
        self.day = 1
        self.am = True


    def main(self):
        """The beginning of everything."""
        self.main_menu()


if __name__ == "__main__":
    game = Main()
    game.main()

