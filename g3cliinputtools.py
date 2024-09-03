import g3encodingjp, os


def get_number_size():
    while True:
        try:
            number_size = int(input("Enter char length needed: "))
        except ValueError as err:
            print(f"Error: {err}")
        else:
            return number_size


def get_user_input():
    while True:
        try:
            number = int(input("Enter a hexadecimal number: "), 16)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            return number
        

def get_box_names():
    box_names = []
    if os.name == 'nt':
        print("Press Ctrl-Z and Enter to exit")
    else:
        print("Press ^D + Enter to exit")
    while True:
        try:
            box_name = list(input("Enter a box name: "))
            for i in range(len(box_name)):
                # Replace chars with Japanese equivalent
                match box_name[i]:
                    case ' ':
                        box_name[i] = '　'
                    case '!':
                        box_name[i] = '！'
                    case '?':
                        box_name[i] = '？'
                    case '/':
                        box_name[i] = '／'
                    case '…':
                        box_name[i] = '‥'
                    case '-':
                        box_name[i] = 'ー'
                    case '–':
                        box_name[i] = 'ー'
                    case '.':
                        box_name[i] = '。'
                    case '“':
                        # Support for straight quotes will never be added as 
                        # trying to guess the context will be too hard
                        box_name[i] = '『'
                    case '”':
                        box_name[i] = '』'
                    case '‘':
                        box_name[i] = '「'
                    case '’':
                        box_name[i] = '」'
            if not(len(box_name) > 8):
                # Ensures that each box name ends with an 0xFF terminator
                while len(box_name) < 9:
                    box_name.append('␃')
                box_names.append(''.join(box_name).encode('G3Encoding'))
            else:
                # Pokémon Box names cannot be more than 8 chars long
                # without hacking.
                raise ValueError(
                    f"Box Name `{''.join(box_name)}` is more than eight characters long"
                )
        except ValueError as err:
            print(f"Error: {err}")
        except UnicodeEncodeError as err:
            print(f"Error: {err}")
        except EOFError:
            # EOFError exception is the most reliable way to end an input
            # loop lasting multiple lines. Press Ctrl-Z + Enter for Windows
            # or press ^D + Enter
            return tuple(box_names)