def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_tracker = {}
    for letter in phrase:
        lower_letter = letter.lower()
        if (lower_letter in "aeiou") and (lower_letter not in vowel_tracker.keys()):
            vowel_tracker[lower_letter] = 1
        elif (lower_letter in vowel_tracker):
            vowel_tracker[lower_letter] += 1
    return vowel_tracker


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
