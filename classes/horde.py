#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Class defining the horde's values."""

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

import random


class Horde:

    def __init__(self):
        self.distance = random.randint(4,7) # Between 4 and 7
        self.size = random.randint(3,6) # Between 3 and 6
