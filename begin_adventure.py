#!/usr/bin/env python3

import cmd, sys, textwrap
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
inventory = ['README Note', 'Small White Stone'] # start with blank inventory
showFullExits = True


print('Welcome to THE GAME.')

#World Dictionaries
worldloc = {
    'Abandoned Town Square': {
        'DESC': 'Light rain falls on rough pavement. Most shops are shuttered. A small stray pig runs by and disappears down a damp alley.',
        'NORTH': 'Main Street',
        'EAST': 'Damp Alley',
        'SOUTH': 'Open Sewer Gate',
        'WEST': 'Broken Shop Window',
        'ITEMS': ['Welcome Sign', 'Fountain']
        },
    'Damp Alley': {
        'DESC': 'Small hoof prints in the mud round a bend ahead and disappear under a fence.',
        'WEST': 'Thief Guild',
        'EAST': 'Bakery',
        'SOUTH': 'Abandoned Town Square',
        'ITEMS': ['Pig']
        }
}

worldItems = {
    'Welcome Sign': {
        'ITEMDESC': 'A welcome sign stands here.',
        'SHORTDESC': 'a welcome sign',
        'LONGDESC': 'The welcome sign reads, "Welcome to this text adventure demo. You can type "help" for a list of commands to use.',
        'TAKEABLE': False,
        'DESCWORDS': ['welcome', 'sign']},
    'Fountain': {
        'ITEMDESC': 'A bubbling fountain of green water.',
        'SHORTDESC': 'a fountain',
        'LONGDESC': 'The water in the fountain is a bright green color. It is full of bubbles, overflowing like a bubble bath.',
        'TAKEABLE': False,
        'DESCWORDS': ['fountain']},
    'Pig': {
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
    """Changes global location"""
    if direction in worldloc[location]:
        print(f"You move {direction}.")
        location = worldloc[location][direction]
        currentLocation(location)
    else:
        print("You cannot move in that direction.")

#start the game
if __name__ == '__main__':
    print('Text Adventure Demo!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    currentLocation(location)
    AdventureCmd().cmdloop()
    print('Thanks for playing!')

## TEMPORARY CODE for testing
while True:
    currentLocation(location)
    response = input()
    if response == 'quit':
        break
    if response in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        moveDirection(response)
