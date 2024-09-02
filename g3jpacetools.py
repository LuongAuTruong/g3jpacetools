#!/usr/bin/env python3
import g3encodingjp


def get_typeable_chars(value : int) -> tuple[int, int]:
    """
    Converts an 8-bit number to a format usable within the constraints of the
    Generation III character encoding. Original algorithm is from Sleipnir17.

    Args:
        value (int): The byte value (0-255).

    Returns:
        tuple: A tuple containing (value_base, value_offset).
    """
    value &= 0xFF
    if 0xB7 <= value < 0xBA:
        return 0xB6, value - 0xB6
    elif 0xEF <= value < 0x100:
        return 0xEE, value - 0xEE
    else:
        return value, 0


def convert_to_typeable(value : bytes) -> tuple[bytes, bytes]:
    base = bytearray()
    offset = bytearray()
    for c in value:
        converted_output = get_typeable_chars(c)
        base.append(converted_output[0])
        offset.append(converted_output[1])
    return bytes(base), bytes(offset)


def show_spaces(string : str) -> str:
    output = []
    for c in string:
        if c == '　':
            output.append('␣')
        else:
            output.append(c)
    return ''.join(output)


def get_display_output(number_array : bytes, separator=" ") -> str:
    string = show_spaces(number_array.decode('G3EncodingJP'))
    return separator.join(c for c in string)


def get_box_name_as_stream(box_names : tuple) -> bytes:
    box_name_stream = bytearray()
    for name in box_names:
        for char in name:
            box_name_stream.append(char)
    return bytes(box_name_stream)


def convert_to_int32(box_names : bytes) -> tuple:
    output = []
    for i in range(0, len(box_names), 4):
        output.append(int.from_bytes(box_names[i:i+4], "little"))
    return tuple(output)


def convert_to_int16(box_names : bytes) -> tuple:
    output = []
    for i in range(0, len(box_names), 2):
        output.append(int.from_bytes(box_names[i:i+2], "little"))
    return tuple(output)