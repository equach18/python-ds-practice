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
    index = 0
    numbers = []
    for row in matrix:
        if len(row) % 2 != 0 and len(row)/2 == index:
            numbers.append(row[index])
        else:
            numbers.append(row[index])
            numbers.append(row[index-1])
        index += 1
    return sum(numbers)
