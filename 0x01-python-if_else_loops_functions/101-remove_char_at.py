#!/usr/bin/python3
# This function creates a copy of the string, removing the character at the posnt

def remove_char_at(input_str, n):
    if n < 0:
        return input_str
    return input_str[:n] + input_str[n+1:]
