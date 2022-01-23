def list_manipulation(lst, command, location, value=None):
    if command == "add":
        if value == None:
            return None
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
    elif command == "remove":
        if location == "beginning":
            lst.pop(0)
            return lst
        elif location == "end":
            lst.pop()
            return lst
    else:
        return None



    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
testList = [1, 2, 3, 4, 5, "Bug"]

print(list_manipulation(testList.copy(), "add", "beginning", "WOOP WOOP"))
print(list_manipulation(testList.copy(), "add", "end", "WOOP WOOP"))
print(list_manipulation(testList.copy(), "add", "end"))
print(list_manipulation(testList.copy(), "add", "typo"))
print(list_manipulation(testList.copy(), "remove", "beginning"))
print(list_manipulation(testList.copy(), "remove", "end"))
print(list_manipulation(testList.copy(), "remove", "typo"))
print(list_manipulation(testList.copy(), "remove", "end", "EXTRA VALUE"))