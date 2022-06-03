#!/usr/bin/python3

from add_0 import add as addf
a = 1
b = 2
def adder(a, b):
    print("{0} + {1} = {2:d}".format(a, b, addf(a,b)))

if __name__ == "__main__":
    adder(a,b)
