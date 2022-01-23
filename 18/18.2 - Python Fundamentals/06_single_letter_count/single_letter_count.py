def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    search_letter = letter.lower()
    formatted_input = word.lower()
    return formatted_input.count(search_letter)

print(single_letter_count('Hello World', 'h'))
print(single_letter_count('Hello World', 'z'))
print(single_letter_count('Hello World', 'l'))
print(single_letter_count('Sometimes, there are things that are beyond my control. But you know what? That is ok. It is ok. We are only human.', 'l'))