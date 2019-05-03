import unittest

from strings import is_anagram, str_to_int

class AnagramsTest(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(is_anagram('racecar', 'racecar'))
        self.assertTrue(is_anagram('', ''))
        self.assertFalse(is_anagram('long', 'long1'))
        self.assertTrue(is_anagram('long1', 'on1lg'))
        self.assertFalse(is_anagram('1', '2'))
        self.assertFalse(is_anagram('one', 'onn'))
        self.assertTrue(is_anagram('cat', 'act'))

class StringsTest(unittest.TestCase):
    def test_basic(self):
        strings = ['444', '-227', '0', '-0', '+0', '123', '321', '-5']
        for string in strings:
            self.assertEqual(int(string), str_to_int(string))

if __name__ == '__main__':
    unittest.main()
