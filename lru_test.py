import unittest
from lru import *

class LRUCacheTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        # Cache size of 2
        cache = LRUCache(2)

        # Nothing should be evicted here:
        cache.set('a', 2)
        cache.set('b', 1)
        self.assertEqual(2, cache.get('a'))
        self.assertEqual(1, cache.get('b'))

        # This should evict `a`:
        cache.set('c', 3)
        self.assertEqual(-1, cache.get('a'))

        # `b` and `c` should still remain:
        for _ in range(2):
            self.assertEqual(1, cache.get('b'))
            self.assertEqual(3, cache.get('c'))

    def test_size_one(self):
        cache = LRUCache(1)
        cache.set('a', 1)
        for _ in range(3):
            self.assertEqual(1, cache.get('a'))
        cache.set('b', 2)
        for _ in range(3):
            self.assertEqual(-1, cache.get('a'))
            self.assertEqual(2, cache.get('b'))

    def test_large_size(self):
        cache = LRUCache(1000)
        for i in range(1000):
            cache.set(str(i), i)
        for i in range(1000):
            self.assertEqual(i, cache.get(str(i)))
        cache.set('1000', 1000)
        self.assertEqual(-1, cache.get('0'))
        self.assertEqual(1, cache.get('1'))
        self.assertEqual(1000, cache.get('1000'))

    def test_updating(self):
        cache = LRUCache(2)
        cache.set('a', 1)
        cache.set('b', 2)
        cache.set('a', 2)
        cache.set('b', 1)
        self.assertEqual(2, cache.get('a'))
        self.assertEqual(1, cache.get('b'))
        cache.set('c', 3)
        self.assertEqual(-1, cache.get('a'))
        self.assertEqual(1, cache.get('b'))
        self.assertEqual(3, cache.get('c'))

if __name__ == '__main__':
    unittest.main()
