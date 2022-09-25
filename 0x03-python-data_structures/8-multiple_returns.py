#!/usr/bin/python3


def multiple_returns(sentence):
    """Return a tuple

    Args:
        sentence: A string to evaluate

    Return:
        Length of the string and and its 1st character
    """

    if sentence:
        return len(sentence), sentence[0]
    else:
        return len(sentence), None


if __name__ == "__main__":
    multiple_returns(sentence)
