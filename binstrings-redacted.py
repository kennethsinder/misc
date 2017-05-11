#!/usr/bin/python
###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-05-10
# Filename: binstrings.py
# Description: Binary string stuff
###########################

def opposite(x: str) -> str:
    return '1' if x == '0' else '0'

def function(x: str, n: int) -> str:
    # REDACTED until 2017-05-17
    return x

def inverse(x: str, n: int) -> str:
    # REDACTED until 2017-05-17
    return x

def generate_up_to(n: int) -> list:
    if n == 0:
        return []
    elif n == 1:
        return ["0", "1"]

    below = generate_up_to(n - 1)
    return list(set(below + ["0" + x for x in below] + ["1" + x for x in below]))

def generate_one_after(n: int) -> list:
    return [x for x in generate_up_to(n + 1) if len(x) == n + 1 and len(''.join(set(x))) > 1]

def are_equal(n: int) -> bool:
    up_to = [function(x, n) for x in generate_up_to(n)]
    one_after = generate_one_after(n)
    result = sorted(up_to) == sorted(one_after)

    up_to = generate_up_to(n)
    one_after = [inverse(x, n) for x in generate_one_after(n)]
    return result and (sorted(up_to) == sorted(one_after))

def main():
    for i in range(1, 20):
        if not are_equal(i):
            print(i)

if __name__ == '__main__':
    main()
