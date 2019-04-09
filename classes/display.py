#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class used to display stuff."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import constants
from classes.player import Player

class Display:


    def title(self):
        """Display the title of the game in ascii art."""
        print("\033[H\033[J") # Clear screen
        print(constants.TITLE)


    def main_menu(self):
        """Displays the first menu when starting the game."""
        print("\n--------------------=:[MAIN MENU]:=--------------------\n")
        print(" [1] Start a new game")
        print(" [2] How to play")
        print(" [3] Exit game")
        print("\n-------------------------------------------------------")


    def intro(self, location):
        """Display the introduction text."""
        print("\033[H\033[J") # Clear screen
        print(constants.INTRO_TEXT % location)


    def help_item(self, help_number):
        """Display the help of the game."""
        help_options = {
                1 : constants.HELP_BASIC,
                2 : constants.HELP_DAY,
                3 : constants.HELP_NIGHT,
        }

        if help_number not in range(1, len(help_options) + 1):
            print("Wrong help number provided.")
            return False

        print(help_options[help_number])


    def help_menu(self):
        """Displays the help menu."""
        print("\n [WHAT DO YOU NEED ?]\n")
        print(" [1] Basic help")
        print(" [2] During the day")
        print(" [3] During the night")
        print(" [4] Exit help")


    def actions_day(self):
        """Displays the actions of the day."""
        print("\n [WHAT WILL YOU DO DURING THE DAY?]\n")
        print(" [1] Scavenge")
        print(" [2] Shoot to reduce the horde")
        print(" [3] Display help")


    def actions_night(self):
        """Displays the night"""
        print("\n [WHAT WILL YOU DO DURING THE NIGHT?]\n")
        print(" [1] Move to the next shelter")
        print(" [2] Stay in the shelter")
        print(" [3] Display help")


    def infos(self, player, horde, day, am):
        """Displays every useful information about the game."""
        print("\n================[YOU]================")
        print("\n* "+player.name)
        print("* Health : "+str(player.health))
        print("* Day : "+str(day))
        if am:
            print("* Period : daytime")
        else:
            print("* Period : dusk")
        print("* State : "+player.state)
        print("\n==============[SHELTER]==============")
        print("\n* "+player.location)
        print("* "+str(player.locations_counter)+"/10")
        print("\n===============[STUFF]===============")
        print("\n* Food : "+str(player.food))
        print("* Ammo : "+str(player.ammo))
        print("\n=====================================")


