import unittest
from lru import *

class LRUCacheTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        cache = LRUCache(2)
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
