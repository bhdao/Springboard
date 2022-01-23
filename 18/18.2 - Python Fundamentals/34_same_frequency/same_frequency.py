def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {}
    freq2 = {}

    def checkity_check(num_in, dict_in):
        for num in str(num_in):
            if num not in dict_in:
                dict_in[num] = 1
            else:
                dict_in[num] += 1

    checkity_check(num1, freq1)
    checkity_check(num2, freq2)
    return freq1 == freq2


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
