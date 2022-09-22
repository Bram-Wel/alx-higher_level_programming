#!/usr/bin/python3
"""This describes a function that prints formated text"""


def text_indentation(text):
    """Prints text in an indented format

    Args:
        text: Text to b printed
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        a = 0
        state = False
        for i in range(len(text)):
            if text[i] in '.?:':
                print(text[a:i + 1])
                print()
                a = i + 2
                state = True
        if i + 1 == len(text) and state is False:
            print(text)
