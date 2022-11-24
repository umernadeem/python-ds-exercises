def three_odd_numbers(nums):
    sum = 0
    for x in range(0,len(nums)-2):
        sum = nums[x] + nums[x+1] + nums[x+2]
        print(sum)
        if sum%2!=0:
            return True
    return False
    
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
