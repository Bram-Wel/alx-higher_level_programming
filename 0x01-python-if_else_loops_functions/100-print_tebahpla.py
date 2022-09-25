#!/usr/bin/python3

inv = 0
for i in reversed(range(97, 123)):
    if inv % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
    inv += 1
