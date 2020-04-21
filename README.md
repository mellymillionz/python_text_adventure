# python_text_adventure

"""
This is the index of all possible items in the game world as 
key-value pairs. 

The items exist in the ITEMS value in an area's entry in the world variable.

The GROUNDDESC value is a short string that displays in the area's description.

The SHORTDESC value is a short string that will be used in sentences like, "You
drop X." or "You buy X."

The LONGDESC value is displayed when the player looks at the item.

The TAKEABLE Boolean value is True if the player can pick up the item and put
it in their inventory.

The DESCWORDS value is a list of strings that can be used in the player's
commands. For example, if this is ['welcome', 'sign'] then the player can type
a command such as "take sign" or "look welcome".

The TAKEABLE value is True if the item can be picked up off the ground. If
this key doesn't exist, it defaults to True.

The EDIBLE value is True if the item can be eaten. If this key doesn't exist,
it defaults to False.