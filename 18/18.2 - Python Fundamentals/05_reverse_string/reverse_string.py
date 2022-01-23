def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    output_string = ""
    for num in range(len(phrase)-1, -1, -1):
        output_string += phrase[num]
    return output_string

print("awesome --> ", reverse_string("awesome"))
print("sauce --> ", reverse_string("sauce"))
print("racecar --> ", reverse_string("racecar"))
print("racecar🏎 --> ", reverse_string("racecar🏎"))