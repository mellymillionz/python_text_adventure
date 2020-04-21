#!/usr/bin/env python3

import cmd, sys, textwrap

#define global variables below
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
ITEMDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'
ITEMS = 'ITEMS'

#Needed for the text wrap module
SCREEN_WIDTH = 80

location = 'Abandoned Town Square' # start in town square
inventory = ['README Note', 'Small White Stone'] # start with blank inventory
showFullExits = True
