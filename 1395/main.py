# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M, T, L
    N, M = map(int, input().split())
    T = [None] * (2 ** (ceil(log2(N)) + 1) - 1)
    L = [None] * (2 ** (ceil(log2(N)) + 1) - 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        b -= 1
        c -= 1
        if a == 0:
            update_range(0, N-1, 1, i, j)
        else:
            query(0, N-1, 1, i, j)

    # ######## INPUT AREA END ############


def update_lazy(s, e, i):
    if L[i] != 0:
        T[i] += (e-s+1) * L[i]

    if s != e:
        L[i*2] += L[i]
        L[i*2+1] += L[i]

    L[i] = 0


def update_range(s, e, i, l, r, diff):
    update_lazy(s, e, i)

    if s > r or e < l:
        return

    if l <= s and e <= r:






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