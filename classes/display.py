#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class used to display stuff."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import os

class Display:


    def title(self):
        """Display the title of the game in ascii art."""
        print("\033[H\033[J") # Clear screen
        print("""
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
        """)
