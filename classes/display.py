#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class used to display stuff."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import constants

class Display:


    def title(self):
        """Display the title of the game in ascii art."""
        print("\033[H\033[J") # Clear screen
        print(constants.TITLE)


    def intro(self, location):
        """Display the introduction text."""
        print(constants.INTRO_TEXT % location)


    def help(self, help_number):
        """Display the help of the game."""
        help_options = {
                1 : constants.HELP_BASIC,
                2 : constants.HELP_DAY,
                3 : constants.HELP_NIGHT
        }
        if help_number not in range(1, len(help_options) + 1):
            print("Wrong help number provided.")
            return False

        print(help_options[help_number])
