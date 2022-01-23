def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    output = ""
    for idx_letter in range(len(phrase)):
        if phrase[idx_letter] == to_swap:
            if phrase[idx_letter].isupper():
                output += phrase[idx_letter].lower()
            else:
                output += phrase[idx_letter].upper()
        else:
            output += phrase[idx_letter]
    return output        

normal_string = "Hello! hH x a B a B b b BBb xX yU"
print("normal string:\n",normal_string)
print(flip_case(normal_string, "H"))
print(flip_case(normal_string, "h"))
print(flip_case(normal_string, "x"))
print(flip_case(normal_string, "X"))
print(flip_case(normal_string, "y"))
print(flip_case(normal_string, "B"))
print(flip_case(normal_string, "BB"))
print(flip_case(normal_string, "b"))