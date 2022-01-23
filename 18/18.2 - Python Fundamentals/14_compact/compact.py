def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [val for val in lst if val]
    # Wow ok I have no idea how this one works

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))