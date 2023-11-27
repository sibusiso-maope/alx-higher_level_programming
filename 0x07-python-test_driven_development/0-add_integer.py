def add_integer(a, b=98):
    """Return the integer sum of a and b

    Float arguments are typecasted to integers before they are added

    Raises:
        TypeError: If either a or b is not an integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be and interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
