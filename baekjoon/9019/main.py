# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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

    T = int(input())
    dp = [None] * 10000
    ans = []
    for i in range(T):
        a, b = map(int, input().split())
        solve(a, b, dp)
        ans.append(buildString(a, b, dp))
    print('\n'.join(ans))

    # ######## INPUT AREA END ############


def buildString(a, b, dp):
    lst = []
    cur = b
    while cur != a:
        prev, l = dp[cur]
        lst.append(l)
        cur = prev
    return ''.join(reversed(lst))


def solve(a, b, dp):
    for i in range(10000):
        dp[i] = None

    dq = deque()
    dq.append(a)
    dp[a] = ""
    #dp[a] = (-1, "")

    while dq and dp[b] == None:
        c = dq.popleft()

        d = c * 2 % 10000
        if dp[d] == None:
            dp[d] = (c, "D")
            dq.append(d)

        s = (c - 1) % 10000
        if dp[s] == None:
            dp[s] = (c, "S")
            dq.append(s)

        q, r = divmod(c, 1000)
        ll = r * 10 + q
        if dp[ll] == None:
            dp[ll] = (c, "L")
            dq.append(ll)

        q, r = divmod(c, 10)
        rr = r * 1000 + q
        if dp[rr] == None:
            dp[rr] = (c, "R")
            dq.append(rr)


# #######
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
