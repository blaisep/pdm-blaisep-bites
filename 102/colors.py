from typing import List

VALID_COLORS: list[str] = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        user_input = input("Enter a color, or quit: ")
        user_input = user_input.lower()
        if user_input == 'quit':
            print(f'bye')
            break
        for color in VALID_COLORS:
            if user_input == color:
                print(color)
                continue
        print(color)
        print('Not a valid color')
        print('bye')
        break
