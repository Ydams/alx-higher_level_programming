#!/usr/bin/python3
# This function creates a copy of the string, removing the character at the posnt

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
