#!/usr/bin/python
###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-08-12
# Filename: strings.py
# Description: String-related routines
###########################

def str_to_int(string):
    """ (str) -> int
    Converts the given string to the integer it represents.
    Assumes value can be safely converted to int, in which case,
    behaviour is identical to the Python built-in int() conversion function.
    """
    result = 0
    for char in string:
        if char != '-' and char != '+':
            result = 10 * result + ord(char) - 48
    if string[0] == '-':
        return -result
    return result

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    dict1, dict2 = {}, {}
    for character in str1:
        if character in dict1:
            dict1[character] += 1
        else:
            dict1[character] = 1
    for character in str2:
        if character in dict2:
            dict2[character] += 1
        else:
            dict2[character] = 1
    return dict1 == dict2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
