#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list

    Args:
        @my_list: list of elements
        @x: No. of elements to print from my_list

    Return: Real no. of elements printed
    """

    try:
        for el in range(x):
            print(my_list[el], end="")
        if (x == 0):
            return (0)
        return (el + 1)
    except IndexError:
        return (el)
    finally:
        print()
