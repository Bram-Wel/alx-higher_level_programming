#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a string copy but removing character at position n"""
    cpy = ""
    c = 0
    for i in str:
        if n == c:
            c += 1
            continue
        cpy += i
        c += 1
    return cpy
