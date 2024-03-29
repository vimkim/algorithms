def main(f = None):
    init(f)
    N = int(input())
    mat = [[int(i)-1 for i in input().split()] for _ in range(N)]

    K = 0
    B = 1
    L = 2

    n2ij = [None] * (N*N)
    for i, j in For(N, N):
        n2ij[mat[i][j]] = (i, j)
    
    dp = nDim(N*N, N, N)
    for i, j, k in For(N*N, N, N):
        dp[i][j][k] = [3, 3, 2]

    def fromTo(start, end):
        x, y = n2ij[start]
        xe, ye = n2ij[end]

        dq = deque()
        curr = start
        dq.append((curr, x, y, K))
        dq.append((curr, x, y, B))
        dq.append((curr, x, y, L))
        dp[curr][x][y] = [0, 0, 0]
        while dq:
            curr, x, y, unitType = dq.popleft()
            if x == xe and y == ye:
                return

            currBoard = dp[curr]
            currStep = currBoard[x][y][unitType]

            target = curr+1
            xt, yt = n2ij[target]

            for i in range(3):
                if i == unitType:
                    continue
                val = currBoard[x][y][i]
                if val > currStep + 1:
                    currBoard[x][y][i] = currStep + 1
                    dq.append((curr, x, y, i))


            if unitType == K:
                pass
            elif unitType == L:
                for i in range(N):
                    if i != x:
                        val = currBoard[i][y][L]
                        val = min(val, currStep+1)
                        currBoard[i][y][L] = val
                for j in range(N):
                    if j != y:
                        val = currBoard[x][j][L]
                        val = min(val, currStep+1)
                        currBoard[x][j][L] = val

            else: # unitType == B
                for i in range(N):
                    if i == x: continue
                    diff = i - x
                    j0 = y - diff
                    j1 = y + diff

                    if 0 <= j0 < N:
                        val = currBoard[i][j0][B]
                        val = min(val, currStep+1)
                        currBoard[i][j0][B] = val
                    if 0 <= j1 < N:
                        val = currBoard[i][j1][B]
                        val = min(val, currStep+1)
                        currBoard[i][j0][B] = val
            nextStage += 1

        return 100
    ans = fromTo(0, N*N-1)
    print(ans)


def nDim(*args, default = None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default = default) for _ in range(args[0])]


def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

# CP template Version 1.005
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, log2, ceil, floor
import math
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline

def init(f = None):
    global input
    input = sys.stdin.readline # by default
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)

# Mod #
class Mod:
    MOD = 10**9 + 7
    maxN = 5
    FACT = [0] * maxN
    INV_FACT = [0] * maxN

    @staticmethod
    def setMOD(n): Mod.MOD = n

    @staticmethod
    def add(x, y): return (x+y) % Mod.MOD

    @staticmethod
    def multiply(x, y): return (x*y) % Mod.MOD

    @staticmethod
    def power(x, y):
        if y == 0: return 1
        elif y % 2: return Mod.multiply(x, Mod.power(x, y-1))
        else:
            a = Mod.power(x, y//2)
            return Mod.multiply(a, a)

    @staticmethod
    def inverse(x): return Mod.power(x, Mod.MOD-2)

    @staticmethod
    def divide(x, y): return Mod.multiply(x, Mod.inverse(y))

    @staticmethod
    def allFactorials():
        Mod.FACT[0] = 1
        for i in range(1, Mod.maxN): Mod.FACT[i] = Mod.multiply(i, Mod.FACT[i-1])

    @staticmethod
    def inverseFactorials():
        n = len(Mod.INV_FACT)
        Mod.INV_FACT[n-1] = Mod.inverse(Mod.FACT[n-1])
        for i in range(n-2, -1, -1): Mod.INV_FACT[i] = Mod.multiply(Mod.INV_FACT[i+1], i+1)

    @staticmethod
    def coeffBinom(n, k):
        if n < k: return 0
        return Mod.multiply(Mod.FACT[n], Mod.multiply(Mod.INV_FACT[k], Mod.INV_FACT[n-k]))
    
    @staticmethod
    def sum(it):
        res = 0
        for i in it: res = Mod.add(res, i)
        return res
# END Mod #

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()