def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)

test_list = [1, 3, 2, 4, 3, "telephone", 3, 3, 4, "apple", "telephone", " ", " ", " "]

print(frequency(test_list, 3))
print(frequency(test_list, 1))
print(frequency(test_list, 2))
print(frequency(test_list, 4))
print(frequency(test_list, "telephone"))
print(frequency(test_list, "apple"))
print(frequency(test_list, " "))