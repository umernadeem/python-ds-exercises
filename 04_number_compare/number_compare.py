def number_compare(a, b):
    if (a>b):
        return "First is greater"
    elif (b>a):
        return "Second is Greater"
    elif (b==a):
        return "Numbers are equal"
    else:
        return "Invalid number"
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """