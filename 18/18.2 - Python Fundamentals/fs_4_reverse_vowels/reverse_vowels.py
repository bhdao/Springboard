def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    reversed_vowels = []
    for char in s[::-1]:
        if (char.lower() in "aeiou"):
            reversed_vowels.append(char)
    new_string = ""
    for char in s:
        if (len(reversed_vowels) > 0) and (char.lower() in "aeiou"):
            new_string += reversed_vowels.pop(0)
        else:
            new_string += char
    return new_string

    # for idx, char in enumerate(s):
    #     if (char.lower() in "aeiou"):
    #         s[idx] = reversed_vowels.pop(-1)
    return s


print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))
