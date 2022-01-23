def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    last_idx = len(nums)
    # initialized exactly +1 index out of range to ensure outer index conditional does not fail the first time
    current_match = ()
    for idx_left_num, left_num in enumerate(nums):
        goal_pair = goal - left_num
        for idx_right_num in range(idx_left_num+1, len(nums)):
            # range begins at index immediately after the
            if(nums[idx_right_num] == goal_pair) and (last_idx > idx_right_num):
                last_idx = idx_right_num
                current_match = (left_num, nums[idx_right_num])
                break
    return current_match


print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
