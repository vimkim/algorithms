import os
import sys
import itertools
import collections
TEST = ''
DEBUG = False
if os.path.exists("i" + TEST):
    DEBUG = True
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def main():
    a = input().rstrip()
    a = list(a)
    import string
    lookupUpper = string.ascii_uppercase * 2
    lookupLower = string.ascii_lowercase * 2

    for i,e in enumerate(a):
        if e.islower():
            a[i] = lookupLower[ord(e)-ord('a')+13]
        elif e.isupper():
            a[i] = lookupUpper[ord(e)-ord('A')+13]

    print(''.join(a))


if __name__ == "__main__":
    main()