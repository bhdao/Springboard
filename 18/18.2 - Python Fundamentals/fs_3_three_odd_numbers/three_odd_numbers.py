def three_odd_numbers(nums):
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
    for idx, num in enumerate(nums[0:len(nums)-2]):
        # Reads up to the 3rd to last item in the list to limit calculations to only what is necessary
        three_num_sum = num + nums[idx+1] + nums[idx+2]
        if three_num_sum % 2 != 0:
            return True
        # Gets sum of current number in list and the two following numbers, returns true if odd
    return False


print(three_odd_numbers([1, 2, 3, 4, 5]))
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print(three_odd_numbers([1, 2, 3, 3, 2]))
