#!/usr/bin/env python3
import g3jpacetools, g3cliinputtools
from g3cliinputtools import get_box_names, get_number_size, get_user_input


def convert_char_to_hex():
    raw_box_names = get_box_names()
    box_name_stream = g3jpacetools.get_box_name_as_stream(raw_box_names)
    box_names_int32 = g3jpacetools.convert_to_int32(box_name_stream)
    box_names_int16 = g3jpacetools.convert_to_int16(box_name_stream)
    raw_display_names = '\n'.join(name.hex(' ') for name in raw_box_names)
    int32_names_display = '\n'.join(f'{i:08X}' for i in box_names_int32)
    int16_names_display = '\n'.join(f'{i:04X}' for i in box_names_int16)
    code_generator_display = '\n'.join(hex(i) for i in box_names_int32)
    print("Raw\n"
          "\n"
          f"{raw_display_names}\n"
          "\n"
          "ARM\n"
          "\n"
          f"{int32_names_display}\n"
          "\n"
          "Thumb\n"
          "\n"
          f"{int16_names_display}\n"
          "\n"
          "CodeGenerator Format\n"
          "\n"
          f"{code_generator_display}")


def convert_hex_to_char():
    number_size = get_number_size()
    number = get_user_input()
    number_bytes = number.to_bytes(number_size, 'little', signed=False)
    number_base, number_offset = g3jpacetools.convert_to_typeable(number_bytes)
    display_number_base = g3jpacetools.get_display_output(number_base)
    display_number_offset = g3jpacetools.get_display_output(number_offset)
    print(f"Base:\t{display_number_base}\n"
          f"Offset:\t{display_number_offset}")


def main():
    while True:
        try:
            print(f"G3 JP ACE tools\n"
                  f" - Hex to Char\n"
                  f" - Char to Hex")
            tool_use = input("Choose a tool: ")
            match tool_use.lower():
                case "hex to char":
                    return convert_hex_to_char()
                case "char to hex":
                    return convert_char_to_hex()
                case _:
                    raise ValueError("Invalid choice")
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == '__main__': main()