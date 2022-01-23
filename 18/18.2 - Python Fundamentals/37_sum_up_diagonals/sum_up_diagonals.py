def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    output_sum = 0
    reverse_idx = len(matrix)-1
    for num in range(len(matrix)):
        output_sum += matrix[num][num]
        output_sum += matrix[num][reverse_idx]
        reverse_idx -= 1

    return output_sum


m1 = [
    [1,   2],
    [30, 40],
]
# Should be 73

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Should be 30

m3 = [
    [2, 1, 1, 1000],
    [1941, 2, 2, 14],
    [9, 2, 2, 56],
    [2, 6, 1, 2],
]
# Should be 1014

m4 = [
    [1, 1000, 1000, 1000, 2000],
    [2, 1, 1000, 1, 1000],
    [1, 2, 1, 8, 8],
    [1, 1, 2, 1, 1],
    [1, 8, 5, 2, 1],
]
# Should be 2009

print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))
print(sum_up_diagonals(m3))
print(sum_up_diagonals(m4))
