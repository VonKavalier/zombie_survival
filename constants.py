#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""constants.py: File containig the constants to facilitate adjustments"""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

# At the beginning
AMMO_START = 2
FOOD_START = 2

# Other constants
DAYS_TO_WIN = 20
LOCATIONS_TO_WIN = 10

# Title of the game
TITLE = """
    ·▄▄▄▄•      • ▌ ▄ ·. ▄▄▄▄· ▪  ▄▄▄ . 
    ▪▀·.█▌▪     ·██ ▐███▪▐█ ▀█▪██ ▀▄.▀·     
    ▄█▀▀▀• ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄▐█·▐▀▀▪▄     
    █▌▪▄█▀▐█▌.▐▌██ ██▌▐█▌██▄▪▐█▐█▌▐█▄▄▌     
    ·▀▀▀ • ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀ ▀▀▀ ▀▀▀      
    .▄▄ · ▄• ▄▌▄▄▄   ▌ ▐·▪   ▌ ▐· ▄▄▄· ▄▄▌  
    ▐█ ▀. █▪██▌▀▄ █·▪█·█▌██ ▪█·█▌▐█ ▀█ ██•  
    ▄▀▀▀█▄█▌▐█▌▐▀▀▄ ▐█▐█•▐█·▐█▐█•▄█▀▀█ ██▪  
    ▐█▄▪▐█▐█▄█▌▐█•█▌ ███ ▐█▌ ███ ▐█ ▪▐▌▐█▌▐▌
     ▀▀▀▀  ▀▀▀ .▀  ▀. ▀  ▀▀▀. ▀   ▀  ▀ .▀▀▀ 
"""

# Texts
INTRO_TEXT = "[The zombie apocalypse started a few days ago. You are a survivor, alone. You managed to hide in %s with food and ammunition. Despite this, zombies surround you and get closer every day.]"

## Help

HELP_BASIC = """
===================[BASIC HELP]======================

The game is divided into days, and each day is divided in two.

Every day you will have a choice between exploring or attacking the horde to reduce it.

At the end of each day you will have the choice between staying in your shelter or move to another one.

You win when you reach your final destination (""" + str(LOCATIONS_TO_WIN) + """th location visited) in less than """ + str(DAYS_TO_WIN) + """ days.
You die when you have no food left.

=====================================================
"""

HELP_DAY = """
===================[DURING THE DAY]==================

* EXPLORATION

    Allows you to scavenge and maybe find food and ammunition.
    The amount found will change depending on how far and how much the zombies are.
    There is a greater or lesser chance running into a zombie, you will have to decide to shoot or run away by losing a ration.

* REDUCE THE HORDE
    
    Your goal is to attack the horde to remove a few zombies and make exploration easier and less risky.
    You will never miss your shot, and can choose how many ammunition to use.
   
=====================================================
"""

HELP_NIGHT = """
==================[END OF DAY]=======================

* STAY IN THE SHELTER

    The zombies will approach a certain distance every day.
    Other zombies will also join the horde.
    Only one ration of food is consumed.

* CHANGE SHELTER
    
    Only possible if you have at least 2 rations.
    The number of places visited increases by 1.
    You also move on to the next day.
    You're not sure you'll succeed, it depends on the distance and size of the horde
    If you miss, you stay and lose 2 rations in addition to the one you need to survive the night. 
    Otherwise
    You use part of your ammunition to guarantee your escape.
    Since you change location, the horde is further away but it's size increases.

=====================================================
"""
