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
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, A, T
    N = int(input())
    A = [int(i) for i in input().split()]
    M = int(input())
    T = [None] * (2 ** (ceil(log2(N))+1))
    build(0, N-1, 1)

    for _ in range(M):
        n, i, j = map(lambda x:int(x)-1, input().split())
        if n == 0:
            j += 1
            update(i, j, 0, N-1, 1)
        elif n == 1:
            print(getMin(i, j, 0, N-1, 1)[1]+1)

    # ######## INPUT AREA END ############



def build(i, j, idx):
    if i == j:
        T[idx] = (A[i], i)
        return T[idx]
    else:
        mid = (i + j) // 2
        T[idx] = min(build(i, mid, 2 * idx), build(mid+1, j, 2 * idx + 1))
        return T[idx]


def update(i, v, s, e, idx):
    if i < s or e < i:
        return T[idx]

    if s == e:
        T[idx] = (v, i)
        return T[idx]
    else:
        mid = (s + e) // 2
        T[idx] = min(update(i, v, s, mid, idx * 2), update(i, v, mid+1, e, idx * 2 + 1))
        return T[idx]


def getMin(i, j, s, e, idx):
    if i <= s <= e <= j:
        return T[idx]

    elif j < s or e < i:
        return (10 ** 15, 10 ** 15)

    else:
        mid = (s + e) // 2
        return min(getMin(i, j, s, mid, idx * 2), getMin(i, j, mid+1, e, idx*2 + 1))







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