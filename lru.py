#/usr/bin/env python

class LRUCache(object):
    """
    We maintain the pre-conditions and post-conditions throughout that,
    len(self.map) == the length of the doubly-linked list referred to
    with the self.head -> self.tail pointers.
    """

    def __init__(self, N):
        self.N = N
        self.head = None
        self.tail = None
        self.map = {}

    def set(self, key, value):
        if key in self.map:
            self.map[key].value = value
            return

        if len(self.map) >= self.N:
            # Evict least recently used node, which
            # is at the tail of the doubly-linked list.
            tail = self._remove(self.tail)
            del self.map[tail.key]

        if not self.head:
            self.head = self.tail = Node(key, value)
        else:
            self.tail.next = Node(key, value, self.tail)
            self.tail = self.tail.next
        self.map[key] = self.tail

    def get(self, key):
        if not key in self.map:
            return -1
        new_head = self.map[key]
        result = new_head.value

        if len(self.map) > 1 and self.head.key != new_head.key:
            # Need to move accessed node up to the front,
            # since it was the most recently used.
            old_head = self.head
            self._remove(new_head)
            old_head.prev = new_head
            self.head = new_head
            new_head.next = old_head

        return result

    def _remove(self, node):
        ptr = self.head
        while ptr != node and ptr:
            ptr = ptr.next
        if ptr.prev:
            ptr.prev.next = ptr.next
        if ptr.next:
            ptr.next.prev = ptr.prev
        if ptr == self.head:
            # Removed first node
            self.head = self.head.next
        if ptr == self.tail:
            # Removed last node
            self.tail = self.tail.prev
        return node

class Node(object):

    def __init__(self, key, value, prev_node=None, next_node=None):
        self.key = key
        self.value = value
        self.prev = prev_node
        self.next = next_node

if __name__ == '__main__':
    pass
