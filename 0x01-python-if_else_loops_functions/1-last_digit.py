#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def abs_no(n):
    """Return the absolute value of number."""
    if n < 0:
        return -n
    return n


num = abs_no(number)
last_digit = num % 10
str0 = f"Last digit of {number} is {last_digit} and is "
if last_digit > 5:
    str1 = f"greater than 5"
elif last_digit == 0:
    str1 = f"0"
else:
    str1 = f"less than 6 and not 0"
print("{}".format(str0 + str1))
