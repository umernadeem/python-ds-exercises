def find_factors(num):
    # factor = []
    # for item in range(1,num+1):
    #     if (num%item==0):
    #         factor.append(item)
    # return factor
    return [n for n in range(1,num+1) if num%n == 0]
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
