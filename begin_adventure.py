#!/usr/bin/env python3

import cmd, textwrap
# import sys
from global_variables import location

# https://raw.githubusercontent.com/asweigart/textadventuredemo/master/snippets/basiccmdloop.py

#define global variables

#define global variables below
DESC = 'DESC'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'
UP = 'UP'
DOWN = 'DOWN'
GROUND = 'GROUND'
SHOP = 'SHOP'
ITEMDESC = 'ITEMDESC'
SHORTDESC = 'SHORTDESC'
LONGDESC = 'LONGDESC'
TAKEABLE = 'TAKEABLE'
EDIBLE = 'EDIBLE'
DESCWORDS = 'DESCWORDS'
ITEMS = 'ITEMS'

SCREEN_WIDTH = 80

location = 'Abandoned Town Square' # start in town square
inventory = ['README Note'] # start with blank inventory
showFullExits = True


print('Welcome to THE GAME.')
print()

#World Dictionaries

worldloc = {'Abandoned Town Square': {
        'DESC': 'A light rain is falling. The square is deserted and the shops are shuttered. In the middle of the square is a large panel with a rusty lever.',
        'NORTH': 'Rusty Panel',
        'EAST': 'Damp Alley',
        'SOUTH': 'Open Sewer Gate',
        'WEST': 'Broken Window',
        'ITEMS': ['tablet']
        },
    'Damp Alley': {
        'DESC': 'Water droplets fall from eaves high above and dark green moss crawls up the stone walls. Small footprints in the mud round a bend ahead and disappear under a fence.',
        'WEST': 'Abandoned Town Square',
        'EAST': 'Wooden Door with poster',
        'SOUTH': 'Hole Under Fence',
        'ITEMS': ['footprints', 'poster']
        },
    'Rusty Panel': {
        'DESC': 'A rusted octagonal panel with a single switch at the center.',
        'WEST': 'Broken Fence',
        'EAST': 'Wooden Door with poster',
        'SOUTH': 'Abandoned Town Square',
        'ITEMS': ['lever']}
}

worldItems = {
    'tablet': {
        'ITEMDESC': 'You have a small tablet in your hand.',
        'SHORTDESC': 'a tablet',
        'LONGDESC': 'When the keypad is pressed, a note appears on the screen. It reads: Stranger - I worry you have arrive too late. This world is not well, but I have attempted to provide some assistance to you with this device. If you are stuck, type "HELLO COMPUTER" and a list of commands will appear. Good luck.',
        'TAKEABLE': False,
        'DESCWORDS': ['keypad', 'note']},
     'poster': {
        'ITEMDESC': 'A poster nailed onto the wooden door.',
        'SHORTDESC': 'a poster',
        'LONGDESC': 'No Trespassing. This building is now property of the S.R.L.',
        'TAKEABLE': False,
        'DESCWORDS': ['poster']},
     'lever': {
        'ITEMDESC': 'A t-shaped lever protrudes from the panel.',
        'SHORTDESC': 'a lever',
        'LONGDESC': 'You move the lever. Its grates under pressure, but you hear a whirring sound. A spherical hologram appears above the terminal. A face womans appears, accompanied by cheering and clapping of thousands of people. The sound echos strangely through the abandoned square.',
        'TAKEABLE': False,
        'DESCWORDS': ['poster']},
    'footprints': {
        'ITEMDESC': 'Tiny cloved hoofprints in the mud.',
        'SHORTDESC': 'hoofprints',
        'LONGDESC': 'They do not look like any animal you recognize. The creature seems to have been running quickly. They dissapear beneath the fence',
        'TAKEABLE': False,
        'DESCWORDS': ['foot', 'prints']},
    'pig': {
        'ITEMDESC': 'A tiny pig peers out from under the fence.',
        'SHORTDESC': 'a pig',
        'LONGDESC': 'His eyes are full of knowledge and understanding. He becons you to follow',
        'TAKEABLE': False,
        'DESCWORDS': ['pig']}
}
# Classes 
class AdventureCmd(cmd.Cmd):
    #prompt printed when the player is expected to begin typing in a command.
    prompt = '\n'

    def callback(self, input):
        print('Cannot compute request. Type "HELLO COMPUTER" for a list of commands')

    def quit(self, input):
        return True



#Define helper functions:


def currentLocation(loc):
    """This function displays info about current location"""
    print(loc)
    print('=' * len(loc))

    #print the location description
    print('\n'.join(textwrap.wrap(worldloc[loc][DESC], SCREEN_WIDTH)))

    #print items available
    if len(worldloc[loc][ITEMS]) > 0:
        print()
        #print the description for each available item
        for item in worldloc[loc][ITEMS]:
            print(worldItems[item][ITEMDESC])
    
    #print exit options
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        #If that exit direction exists in the location dictionary
        if direction in worldloc[loc].keys():
            exits.append(direction.title()) #doesnt really need to be capitalized
    
    print()
    if showFullExits: #this is a method from Class.
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            #here, location variable refers to the global town square
            if direction in worldloc[location]:
                print('%s: %s' % (direction.title(), worldloc[location][direction]))
    
    #If none of those options are available, print the exit options
    else:
        print('Exits: %s' % ' '.join(exits))
    
def moveDirection(direction):
    """Changes the players location"""
    global location

    if direction in worldloc[location]:
        print(f"You move {direction}.")
        location = worldloc[location][direction]
        currentLocation(location)
    else:
        print("You cannot move in that direction.")

def do_north(self, arg):
        """Go to the area to the north, if possible."""
        moveDirection('north')

def do_south(self, arg):
        """Go to the area to the south, if possible."""
        moveDirection('south')

def do_east(self, arg):
        """Go to the area to the east, if possible."""
        moveDirection('east')

def do_west(self, arg):
        """Go to the area to the west, if possible."""
        moveDirection('west')

## Examine Items


## TEMPORARY CODE for testing
while True:
    currentLocation(location)
    response = input()
    if response == 'quit':
        break
    if response in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        moveDirection(response)
    if response == 'ITEMS':
        print ()

#start the game
# if __name__ == '__main__':
#     print('Text Adventure Demo!')
#     print('====================')
#     print()
#     print('(Type "HELLO COMPUTER" for commands.)')
#     print()
#     currentLocation(location)
#     AdventureCmd().cmdloop()
#     print('Thanks for playing!')


