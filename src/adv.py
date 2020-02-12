from room import Room
from player import Hero

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Hero('Dave', '6ft', 30, 'Mong', 100, room['outside'])

# Write a loop that:
#n
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
x = 'a'
while x != 'q':
    if player.room.name == 'Outside Cave Entrance':
        print(player.room.name, ':', player.room.description, '\n')
        x = input('Please Enter Direction you wish to go, or q to quit: \n')
        if x == 'n':
            player.room = player.room.n_to
        else:
            print('You can only enter the cave [n]s')
    elif player.room.name == 'Foyer':
        print(player.room.name, ':', player.room.description, '\n')
        x = input('Please Enter Direction you wish to go, or q to quit: \n')
        if x == 'n' or 's' or 'e':
            if x == 'n':
                player.room = player.room.n_to
            elif x == 's':
                player.room = player.room.s_to
            elif x == 'e':
                player.room = player.room.e_to
        else:
            print('You can only go east[e] north[n] or south[s]')               
    elif player.room.name == 'Grand Overlook':
        print(player.room.name, ':', player.room.description, '\n')
        x = input('Please Enter Direction you wish to go, or q to quit: \n')
        if x == 's':
            player.room = player.room.s_to
        else:
            print('You can only go south[s]')
    elif player.room.name == 'Narrow Passage':
        print(player.room.name, ':', player.room.description, '\n')
        x = input('Please Enter Direction you wish to go, or q to quit: \n')
        if x == 'w' or 'n':
            if x == 'w':
                player.room = player.room.w_to
            elif x == 'n':
                player.room = player.room.n_to    
        else:
            print('You can only go West[w] or North[n]')
    elif player.room.name == 'Treasure Chamber':
        print(player.room.name, ':', player.room.description, '\n')
        x = input('Please Enter Direction you wish to go, or q to quit: \n')
        if x == 's':
            player.room = player.room.s_to
        else:
            print('There is literally one door ffs[s]')    
