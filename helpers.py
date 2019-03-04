#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Helpers"""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import constants


def check_choice(choices):
    choice = None
    error = False
    while choice is None:
        try:
            choice = int(input("\n> "))
        except ValueError:
            error = True
        else:
            choice = check_range(choice, choices)
    return choice


def check_range(choice, choices):
    while choice not in range(1, choices+1):
        print(constants.CHOICE_NOT_VALID)
        try:
            choice = int(input("\n> "))
        except ValueError:
            check_choice(choices)
    return choice
