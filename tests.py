#!/usr/bin/env python2.7

from os import system

# Menu structure
menu = {0: {1: 'Manage virtual Hosts',
            2: 'Configure PHP-Pools',
            3: 'Manage MySQL Databases',
            4: 'Manage Email-Accounts',
            5: 'Exit'},
        1: {1: 'Create virtual Host',
            2: 'Remove virtual Host',
            3: 'Disable virtual Host',
            4: 'Enable virtual Host',
            5: '<< Go Back'},
        2: {1: 'Create PHP Pool',
            2: 'Remove PHP Pool',
            3: 'Disable PHP Pool',
            4: 'Enable PHP Pool',
            5: '<< Go Back'},
        3: {1: 'Create database',
            2: '<< Go Back'},
        4: {1: 'Create mailbox',
            2: 'Remove mailbox',
            3: 'Disable mailbox',
            4: 'Enable mailbox',
            5: 'Create alias',
            6: 'Remove alias',
            7: 'Disable alias',
            8: 'Enable alias',
            9: '<< Go Back'}}

# Helper Function to print the menu
def print_menu(menu):
    system('cls')

    for entry in options: 
        print entry, menu[entry]

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return False

# Initialize
cur_menu = menu[0]
sel_1 = None
sel_2 = None

while True:   
    options = cur_menu.keys()
    options.sort()

    # Print Options
    print_menu(cur_menu)
    
    # Ask for input
    if sel_1 == None:
        sel_1 = convert_to_int(raw_input("\n> Please choose: "))
    elif sel_2 == None:
        sel_2 = convert_to_int(raw_input("\n> Please choose: "))

    # Handle selection
    if sel_1 in range(1, len(menu)):
        cur_menu = menu[sel_1]

    if   sel_1 == 1:
        if sel_2 == 1:
            sel_2 = None
            print "We will create a virtual Host...done \n"
            raw_input("Press a key to continue...")

        elif sel_2 == 2:
            sel_2 = None
            print "We will delete a virtual Host...done \n"
            raw_input("Press a key to continue...")

        elif sel_2 == 5:
            cur_menu = menu[0]
            sel_1 = None
            sel_2 = None

        elif sel_2 == False:
            print "Error: Invalid input, Loser!"
            break
            
    elif sel_1 == 2:
        print "PHP-POOLS"
        
        if sel_2 == 5:
            cur_menu = menu[0]
            sel_1 = None
            sel_2 = None

    elif sel_1 == 3:
        print "MYSQL"
        
        if sel_2 == 2:
            cur_menu = menu[0]
            sel_1 = None
            sel_2 = None

    elif sel_1 == 4: 
        print "EMAIL"

        if sel_2 == 9:
            cur_menu = menu[0]
            sel_1 = None
            sel_2 = None
        
    elif sel_1 == 5:
        print "Good bye."
        break

    else:
        print "Error: Invalid input, Loser!"
        break
