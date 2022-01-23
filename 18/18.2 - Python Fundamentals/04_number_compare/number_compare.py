def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    outcomes = {
        "a":"First is greater",
        "b":"Second is greater",
        "c":"Numbers are equal",
    }

    if a > b:
        return outcomes["a"]
    elif a < b:
        return outcomes["b"]
    elif a == b:
        return outcomes["c"]

print(number_compare(1, 1))
print(number_compare(1*2/2-1+1, 1/2*2+1-1))
print(number_compare(-1, 1))
print(number_compare(1, -2))
print(number_compare(125, 125.00001))
print(number_compare(125.000005+0.000005, 125.00001))
print(number_compare(12057125*142, -125.00001))