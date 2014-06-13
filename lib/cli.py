from os import system


# Helper Function to print the menu
def print_menu(menu):
    system('cls')

    options = menu.keys()
    options.sort()

    for entry in options:
        print entry, menu[entry]

# Helper Function to get user input
def get_raw_input(prompt = '', required = False, default = '', allowed = []):
  userinput = ''

  # Prepare allowed values for output
  if len(allowed) > 0:
    items = ''

    for i in range(0, len(allowed)):
      if i == 0:
        items = allowed[i]
      else:
        items = items + '/' + allowed[i]

    prompt = prompt + ' [' + items + ']'

  # Prepare the default value
  if default != '':
    prompt = prompt + ' (Default: ' + default + '): '
  else:
    prompt = prompt + ': '

  # Ask for input
  if required == True or len(allowed) > 0:
    while len(userinput) == 0:
      userinput = raw_input(prompt) or default
  else:
    userinput = raw_input(prompt) or default

  return userinput