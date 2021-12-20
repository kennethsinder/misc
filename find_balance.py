from typing import List

def find_balance(L: List[int]) -> List[int]:
    """
    >>> find_balance([0, 0, 0])
    [3, 2, 1]
    >>> find_balance([0, 2, -8, 7, -7, 1, 7])
    [1, 0, 5, 2, 0, 0, 0]
    >>> find_balance([-4, -5, 3, 6, -2, 6, -4, -2, 2])
    [9, 0, 0, 0, 5, 3, 0, 2, 0]
    """
    result = [0] * len(L)
    for i in range(len(L)):
        total = 0
        for j in range(i, len(L)):
            total += L[j]
            if not total:
                result[i] = j - i + 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

