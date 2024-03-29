# CP template Version 1.4

# time complexity: O(NlogN + M*MlogM)
def solution(words, queries): # N = len(words) # M = len(queries)
    from bisect import bisect_left, bisect_right
    prefix = [(len(x), x) for x in words] # O(N)
    prefix.sort() # O(NlogN)
    postfix = [(len(x), x[::-1]) for x in words] # O(NlogN)
    postfix.sort()
    ans = []
    for query in queries: # O(M * MlogM)
        ln = len(query)
        q = (ln, query)
        usedArray = prefix
        if query[0] == '?' or query[-1] == '?':
            queryPre = query.replace('?', 'a')
            queryPost = query.replace('?', 'z')
            if query[0] == '?':
                qPre = (ln, queryPre[::-1])
                qPost = (ln, queryPost[::-1])
                usedArray = postfix
            else:
                qPre = (ln, queryPre)
                qPost = (ln, queryPost)
        else:
            qPre, qPost = q, q
        iB = bisect_left(usedArray, qPre) # O(MlogM)
        iE = bisect_right(usedArray, qPost) # O(MlogM)
        ans.append(iE - iB)

    return ans

def main(f = None):
    hello = [1, 2]
    x = 5
    heappush(hello, x)
    init(f)
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    #queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    queries = ["frodo", "fro??", "????o", "fr???", "fro???", "pro?"]
    ans = solution(words, queries)
    print(ans)
    result = [1, 3, 2, 4, 1, 0]
    assert ans == result

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
    input=sys.stdin.readline

def init(f = None):
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