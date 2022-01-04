def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    final_sum = 0
    for num in nums:
      final_sum += num
    return final_sum

print("sum_nums returned", sum_nums([1, 2, 3, 4, 26, 52, 31, 21, 3, 4, 5, 5, 5, 90]))
