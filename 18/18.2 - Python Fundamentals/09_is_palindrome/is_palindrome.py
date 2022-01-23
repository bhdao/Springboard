def is_palindrome(phrase):
    phrase = phrase.lower()
    reverse = ""
    for letter in range(len(phrase)-1, -1, -1):
        reverse += phrase[letter]
    return (reverse == phrase)

print(is_palindrome("ooo"))
print(is_palindrome("racecar"))
print(is_palindrome("raCecaR"))
print(is_palindrome("boot"))
print(is_palindrome("boot👢toob"))