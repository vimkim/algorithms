# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


fact = [1] * 1000

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M
    N, M = map(int, input().split())

    # ######## INPUT AREA END ############

    num5 = cntHowManyXAppearsFromFactN(N, 5)\
        - cntHowManyXAppearsFromFactN(M, 5)\
            - cntHowManyXAppearsFromFactN(N-M, 5)

    num2 = cntHowManyXAppearsFromFactN(N, 2)\
        - cntHowManyXAppearsFromFactN(M, 2)\
            - cntHowManyXAppearsFromFactN(N-M, 2)

    print(min(num2, num5))




def comb(n, m):
    return fact[n] // fact[m] // fact[n-m]


def cntHowManyXAppearsFromFactN(n, x):
    cnt = 0
    i = x
    while i <= n:
        cnt += n // i
        i *= x
    return cnt




# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()