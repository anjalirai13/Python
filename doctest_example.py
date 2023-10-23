import doctest


def doctest_1():
    """ 
    Testing doctest module. Doctest module runs the interpreter lines from the file
    and next line should be the result of the above command and it will verify that
    :return: Hello Python! Testing Doctest.
    >>> print("Hello Python! Testing Doctest.")
    Hello Python! Testing Doctest.
    """


def doctest_2():
    """
    Testing doctest module. Doctest module runs the interpreter lines from the file
    and next line should be the result of the above command and it will verify that.
    This function will fail becasue next and print statement result is not same.
    :return: Hello Python! Testing Doctest.
    >>> print("Hello Python! Testing Doctest.")
    Hello Python!.
    """


if __name__ == "__main__":
    doctest.testmod()