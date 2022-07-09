#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints integers in 1st  x elements of a list

    Args:
        @my_list: List of elements
        @x: No of elements to print

    Return:
        No. of integers printed
    """

    count = 0
    for el in range(x):
       try:
           print("{:d}".format(my_list[el]), end='')
           count += 1

       except TypeError:
           continue
       except ValueError:
           pass
    print()

    return (count)


if __name__ == "__main__":
    safe_print_list_integers(my_list, x)
