def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    greaters_output = 0
    for idx, num in enumerate(nums):
        # print(num, "startNum")
        if (idx+1 < len(nums)):
            for after_nums in nums[idx+1:]:
                if num < after_nums:
                    greaters_output += 1

    return greaters_output


print(find_greater_numbers([1, 2, 3])
      )
print(find_greater_numbers([6, 1, 2, 7])
      )
print(find_greater_numbers([5, 4, 3, 2, 1])
      )
print(find_greater_numbers([])
      )
