#!/usr/bin/python
###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-08-08
# Filename: matrix_bfs.py
# Description: Discover groups of colours in a matrix
###########################

from queue import Queue

def in_range(M, i, j):
    """ (list, int, int) -> bool
    Returns True iff (i, j) is within M.
    >>> in_range([], 0, 0)
    False
    >>> in_range([[1, 2], [3, 4]], 1, 0)
    True
    """
    if not M:
        return False
    return i >= 0 and j >= 0 and i < len(M) and j < len(M[0])

def colours(M):
    """
    Returns a dictionary mapping all of the distinct entries of the
    two-dimensional array M to the number of groupings of that entry within M.
    >>> colours([])
    {}
    >>> colours([["Red", "Green", "Green"], ["Red", "Green", "Green"]])["Red"]
    1
    >>> colours([["Red", "Green", "Green"], ["Red", "Green", "Green"]])["Green"]
    1
    >>> colours([["Red", "Blue"], ["Blue", "Red"]])["Red"]
    2
    >>> "Green" in colours([["Red", "Blue"], ["Blue", "Red"]])
    False
    """
    # If the matrix is empty, return an empty dictionary (no colours)
    result = {}
    if M == []:
        return result

    next_colour = (0, 0)   # Maintain the (i, j) position of the next new undiscovered colour
    visited = set([next_colour])   # Maintain a set of visited matrix positions for BFS
    while 1:
        current_colour = M[next_colour[0]][next_colour[1]]    # Determine the current colour being explored
        if current_colour in result:
            result[current_colour] += 1     # Increment the number of groups of that colour
        else:
            result[current_colour] = 1
        q = Queue()     # Queue of neighbour positions for BFS
        q.put(next_colour)
        visited.add(next_colour)
        next_colour = None     # A None value for next_colour represents no more colour groups to explore
        while not q.empty():
            current = q.get()   # Possible neighbours are below, above, left, or right
            neighbours = [(current[0], current[1]-1), (current[0]-1, current[1]),
                          (current[0], current[1]+1), (current[0]+1, current[1])]
            for n in neighbours:    # Check if there are any new colours left in the matrix
                if in_range(M, n[0], n[1]) and M[n[0]][n[1]] != current_colour and not n in visited:
                    next_colour = n
                    break
            # Only look at neighbours of the same colour
            neighbours = [n for n in neighbours if in_range(M, n[0], n[1]) and M[n[0]][n[1]] == current_colour]
            for n in neighbours:
                if not n in visited:
                    visited.add(n)      # BFS algorithm - add (i, j) position to queue and visited set
                    q.put(n)
        if next_colour is None:    # If no new colours were found, the matrix is fully explored
            break

    return result

if __name__ == '__main__':
    # Perform test cases that appear in the above docstrings
    import doctest
    doctest.testmod()
