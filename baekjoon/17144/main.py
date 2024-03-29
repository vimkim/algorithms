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

    global R, C, T, m, purifier
    R, C, T = map(int, input().split())

    m = [list(map(int, input().split())) for _ in range(R)]

    purifier = None
    for i in range(R):
        if m[i][0] == -1:
            purifier = i
            break

    for _ in range(T):
        m = disperse(m)
        m = purify(m)

    sum_ = 0
    for i in range(R):
        for j in range(C):
            if m[i][j] > 0:
                sum_ += m[i][j]
    print(sum_)

    # ######## INPUT AREA END ############


def purify(m):

    # upper
    # col 0
    for i in range(purifier-1, 0, -1):
        m[i][0] = m[i-1][0]
    # row 0
    for i in range(0, C-1):
        m[0][i] = m[0][i+1]

    # col C-1
    for i in range(0, purifier):
        m[i][C-1] = m[i+1][C-1]

    # row purifier
    for i in range(C-1, 1, -1):
        m[purifier][i] = m[purifier][i-1]
    m[purifier][1] = 0

    # lower
    # col 0
    for i in range(purifier+2, R-1):
        m[i][0] = m[i+1][0]

    # row R-1
    for i in range(C-1):
        m[R-1][i] = m[R-1][i+1]

    # col C-1
    for i in range(R-1, purifier + 1, -1):
        m[i][C-1] = m[i-1][C-1]

    # row purifier + 1
    for i in range(C-1, 1, -1):
        m[purifier+1][i] = m[purifier+1][i-1]
    m[purifier+1][1] = 0
    return m




D = ((-1, 0), (1, 0), (0, 1), (0, -1))
def disperse(m):
    nm = [i[:] for i in m]

    for i in range(R):
        for j in range(C):
            if m[i][j] > 0:
                disperseAmount = m[i][j] // 5
                directionCount = 0
                for di, dj in D:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if m[ni][nj] >= 0:
                            directionCount += 1
                            nm[ni][nj] += disperseAmount
                nm[i][j] -= disperseAmount * directionCount
    return nm




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