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

    global N, M, C, F, G, S, E
    N, M = map(int, input().split())

    C = Mat(2*N, 2*N, 0)
    F = Mat(2*N, 2*N, 0)

    G = [[] for _ in range(2*N)]

    for i in range(N):
        C[i*2][i*2+1] = 1
        G[i*2].append(i*2+1)
        G[i*2+1].append(i*2)


    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        aIn = a * 2
        aOut = a * 2 + 1
        bIn = b * 2
        bOut = b * 2 + 1

        C[aOut][bIn] = 1
        C[bOut][aIn] = 1

        G[aOut].append(bIn)
        G[bIn].append(aOut)
        G[bOut].append(aIn)
        G[aIn].append(bOut)

    # ######## INPUT AREA END ############

    S = 0 * 2 + 1
    E = 1 * 2

    totalFlow = 0
    while True:

        P = bfs()
        if P is not None:
            flow = 10 ** 9

            curr = E
            while curr != S:
                prev = P[curr]
                flow = min(flow, C[prev][curr] - F[prev][curr])
                curr = prev

            curr = E
            while curr != S:
                prev = P[curr]
                F[prev][curr] += flow
                F[curr][prev] -= flow
                curr =prev

            totalFlow += flow
        else:
            break
    print(totalFlow)


# TEMPLATE ###############################


def bfs():
    P = [None] * (N*2)

    dq = deque()
    dq.append(S)
    P[S] = S

    while dq:
        x = dq.popleft()

        for y in G[x]:
            if P[y] is not None: continue
            if C[x][y] > F[x][y]:
                P[y] = x
                if y == E:
                    return P
                dq.append(y)
    return None


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