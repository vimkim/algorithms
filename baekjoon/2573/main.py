import os
import sys
import itertools
import collections
import string
# not for python < 3.9
# from functools import cmp_to_key, reduce, partial, cache
from functools import cmp_to_key, reduce, partial
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global N, M, mat, vis, orig
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    vis = Mat(N, M)
    orig = Mat(N, M)

    # ######## INPUT AREA END ############
    # ####################################

    step = 0
    while True:
        step += 1
        melt()
        #parr(mat)

        num = numOfIsland()
        #print(num)
        if num != 1:
            break

    if num == 0:
        print(0)
    else:
        print(step)


def melt():
    global mat, orig
    for i, j in For(N, M):
        orig[i][j] = mat[i][j]


    for i, j in For(N, M):
        val = orig[i][j]
        if val:
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    if orig[ni][nj] == 0:
                        cnt += 1
            val = max(0, val - cnt)
            mat[i][j] = val

def numOfIsland():
    global vis

    for i, j in For(N, M):
        if mat[i][j]:
            vis[i][j] = True
        else:
            vis[i][j] = False


    cnt = 0
    stack = []
    for i, j in For(N, M):
        if vis[i][j]:
            vis[i][j] = False
            cnt += 1
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    ni, nj = x + di[d], y + dj[d]
                    if 0 <= ni < N and 0 <= nj < M:
                        if vis[ni][nj]:
                            vis[ni][nj] = False
                            stack.append((ni, nj))

    return cnt









# #############################################################################
# #############################################################################
# ############################## TEMPLATE AREA ################################
# #############################################################################
# #############################################################################

enu = enumerate


def argmax(arr):
    return max(enumerate(arr), key=lambda x: x[1])


def argmin(arr):
    return min(enumerate(arr), key=lambda x: x[1])


def For(*args):
    return itertools.product(*map(range, args))


def copy2d(mat):
    return [row[:] for row in mat]


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


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
