# import numpy as np

# import pandas

# import matplotlib.pyplot as plt

# def bad_function(x, y):
#     result = x + y
#     return result


# def another_bad_function():
#     x = 10
#     y = 20
#     return x + y


# def main():
#     print(bad_function(10, 20))
#     print(another_bad_function())


# if __name__ == "__main__":
#     main()


def bad_function(x, y):
    """
    This function is bad because it does not have a blank line
    before the docstring.
    """
    result = x + y
    return result


def another_bad_function():
    """This function is bad because it does not have a docstring."""
    x = 10
    y = 20
    return x + y


def main():
    """
    This is the main function of the program.
    It calls the `bad_function` and `another_bad_function` functions
    and prints their results.
    """
    print(bad_function(10, 20))
    print(another_bad_function())


if __name__ == "__main__":
    main()
