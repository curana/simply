from os import system
import lib.cli as cli
import lib.utilities as utils
import lib.handler.vhosts as vhosts


# Constants
HDL_EXIT  = 0
HDL_VHOST = 1
HDL_PHP   = 2
HDL_MYSQL = 3
HDL_EMAIL = 4


def main():
    # Initialize
    menu = menu_cur = { HDL_EXIT:  'EXIT',
                        HDL_VHOST: 'Manage virtual Hosts',
                        HDL_PHP:   'Configure PHP-Pools',
                        HDL_MYSQL: 'Manage MySQL Databases',
                        HDL_EMAIL: 'Manage Email-Accounts' }
    menu_lvl_1 = None
    menu_lvl_2 = None

    
    while True:
        # Show menu
        cli.print_menu(menu_cur)

        # Ask for input
        if menu_lvl_1 == None:
            menu_lvl_1 = utils.convert_to_int(raw_input("\n> Please choose: "))
        elif menu_lvl_2 == None:
            menu_lvl_2 = utils.convert_to_int(raw_input("\n> Please choose: "))


        # Handle menu selection
        if menu_lvl_1 == HDL_VHOST:
            # Set handler submenu
            menu_cur = vhosts.Vhosts.menu

            if menu_lvl_2 == vhosts.Vhosts.HDL_CREATE:
                try:
                    task = vhosts.Vhosts().create()
                    raw_input("Press a key to continue...")
                except KeyboardInterrupt:
                    menu_lvl_1 = None

            elif menu_lvl_2 == vhosts.Vhosts.HDL_REMOVE:
                try:
                    task = vhosts.Vhosts().remove()
                    raw_input("Press a key to continue...")
                except KeyboardInterrupt:
                    menu_lvl_1 = None

            elif menu_lvl_2 == HDL_EXIT: # exit
                menu_cur = menu
                menu_lvl_1 = None

            elif menu_lvl_2 == False:
                print "Error: Invalid input, Loser!"
                break

            menu_lvl_2 = None

        elif menu_lvl_1 == HDL_PHP:
            print "PHP-POOLS"

            if menu_lvl_2 == HDL_EXIT: # exit
                menu_cur = menu
                menu_lvl_1 = None

            menu_lvl_2 = None

        elif menu_lvl_1 == HDL_MYSQL:
            print "MYSQL"

            if menu_lvl_2 == HDL_EXIT: # exit
                menu_cur = menu
                menu_lvl_1 = None

            menu_lvl_2 = None

        elif menu_lvl_1 == HDL_EMAIL:
            print "EMAIL"

            if menu_lvl_2 == HDL_EXIT: # exit
                menu_cur = menu
                menu_lvl_1 = None

            menu_lvl_2 = None

        elif menu_lvl_1 == HDL_EXIT:
            print 'Good bye.'
            break

        else:
            print "Error: Invalid input, Loser!"
            break

# Prevent SignalErrors
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass