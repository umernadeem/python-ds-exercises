def list_check(lst):
    default = False
    for items in lst:
        if isinstance(items,list):
            default = True
        else:
            default = False
    return default
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
