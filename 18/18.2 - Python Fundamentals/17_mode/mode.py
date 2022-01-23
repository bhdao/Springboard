def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    greatest_num = (0, 0)
    mode = {}
    for num in nums:
        if num not in mode:
            mode[num] = 1
        elif num in mode:
            mode[num] += 1
    for (key, val) in mode.items():
        if val > greatest_num[0]:
            greatest_num = (val, key)
    return greatest_num[1]


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
