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

def main():
    strings = ['444', '-227', '0', '-0', '+0', '123', '321', '-5']
    for string in strings:
        if str_to_int(string) != int(string):
            print("ERROR: {0} (actual) != {1} (expected)".format(str_to_int(string), int(string)))
        else:
            print("SUCCESS: {0}".format(string))

if __name__ == '__main__':
    main()
