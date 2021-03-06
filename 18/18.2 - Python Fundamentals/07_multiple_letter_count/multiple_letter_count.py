def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    diccionario = {}
    for letter in phrase:
        if letter not in diccionario.keys():
            diccionario[letter] = 1
        elif letter in diccionario.keys():
            diccionario[letter] += 1
    return diccionario

print(multiple_letter_count("yay"))
print(multiple_letter_count("Yay"))
print(multiple_letter_count("supercalafragilisticexpialidocious"))