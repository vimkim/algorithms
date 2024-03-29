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

    G = [[] for _ in range(58)]
    C = Mat(58, 58, 0)
    #F = Mat(58, 58, 0)

    N = int(input())
    for _ in range(N):
        a, b, v = input().split()
        a = ord(a) - ord('A')
        b = ord(b) - ord('A')
        v = int(v)
        G[a].append(b)
        G[b].append(a)

        C[a][b] += v
        C[b][a] += v

    # ######## INPUT AREA END ############
    s = 0
    t = 25
    global P
    P = [-1] * 58

    totalFlow = 0
    while True:
        for i in range(58):
            P[i] = -1
        P[s] = -2

        # bfs(s)
        dq = deque()
        dq.append(s)

        while dq:
            v = dq.popleft()
            for nbr in G[v]:

                if P[nbr] == -1 and C[v][nbr] > 0:
                    P[nbr] = v
                    dq.append(nbr)
                    if nbr == t:
                        break

        if P[t] == -1:
            break

        curr = t
        flow = 10 ** 9
        while curr != s:
            prev = P[curr]
            flow = min(flow, C[prev][curr])
            curr = prev
        totalFlow += flow

        curr = t
        while curr != s:
            prev = P[curr]
            C[prev][curr] -= flow
            C[curr][prev] += flow
            curr = prev

    print(totalFlow)






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