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
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, L, A, T
    N, L = map(int, input().split())
    A = [int(i) for i in input().split()]

    # ######## INPUT AREA END ############

    T = [None] * (4 * N)
    initTree(0, N-1, 1)

    ans = []

    for i in range(N):
        ans.append(query(0, N-1, i-L+1, i, 1))

    print(' '.join(map(str, ans)))


def initTree(s, e, idx):
    if s == e:
        T[idx] = A[s]
        return T[idx]

    mid = ( s + e ) // 2
    x = initTree(s, mid, idx * 2)
    y = initTree(mid+1, e, idx * 2 + 1)
    T[idx] = min(x, y)
    return T[idx]


def query(s, e, l, r, idx):

    if e < l or r < s:
        return 10 ** 9

    if l <= s and e <= r:
        return T[idx]

    mid = (s + e) // 2
    x = query(s, mid, l, r, idx * 2)
    y = query(mid+1, e, l, r, idx * 2 + 1)
    return min(x, y)



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