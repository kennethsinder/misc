###########################
# Programmer: Kenneth Sinder
# Date Created: 2018-02-11
# Filename: bst.py
# Description: Practice with trees
###########################

class Node:
    def __init__(self, val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def treeify(L):
        """ (list of int) -> Node
        Converts given list to BST
        >>> print(Node.treeify([]))
        None
        >>> print(Node.treeify([2]).val); print(Node.treeify([2]).left); print(Node.treeify([2]).right)
        2
        None
        None
        """
        def recurse(L):
            if not L: return None
            if len(L) == 1:
                return Node(L[0])
            return Node(L[len(L)/2], recurse(L[:len(L)/2]), recurse(L[len(L)/2+1:]))
        return recurse(sorted(L))

def num_in_interval(root, l, r):
    """ (Node, int, int) -> int
    Returns number of nodes rooted at `root` with `val`s
    between `l` and `r`.
    >>> num_in_interval(None, -1000, 1000)
    0
    >>> num_in_interval(Node(10), 9, 12)
    1
    >>> num_in_interval(Node(0, Node(-1), Node(1)), 0, 2)
    2
    """
    if root is None: return 0
    result = 1 if l <= root.val <= r else 0
    if l <= root.val: result += num_in_interval(root.left, l, r)
    if r >= root.val: result += num_in_interval(root.right, l, r)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
