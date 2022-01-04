def in_range(nums, lowest, highest):
    """Print numbers inside range.
    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print
    """

    for num in nums:
      if num <= highest and num >= lowest:
        print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 40)            
