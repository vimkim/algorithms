# CP template Version 1.4
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, ceil, floor
from enum import Enum

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

# Standard IO #
### from io import BytesIO, IOBase
### BUFSIZE = 8192
### class FastIO(IOBase):
###     newlines = 0
###     def __init__(self, file):
###         self._fd = file.fileno()
###         self.buffer = BytesIO()
###         self.writable = "x" in file.mode or "r" not in file.mode
###         self.write = self.buffer.write if self.writable else None
### 
###     def read(self):
###         while True:
###             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
###             if not b:
###                 break
###             ptr = self.buffer.tell()
###             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
###         self.newlines = 0
###         return self.buffer.read()
### 
###     def readline(self):
###         while self.newlines == 0:
###             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
###             self.newlines = b.count(b"\n") + (not b)
###             ptr = self.buffer.tell()
###             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
###         self.newlines -= 1
###         return self.buffer.readline()
### 
###     def flush(self):
###         if self.writable:
###             os.write(self._fd, self.buffer.getvalue())
###             self.buffer.truncate(0), self.buffer.seek(0)
### 
### class IOWrapper(IOBase):
###     def __init__(self, file):
###         self.buffer = FastIO(file)
###         self.flush = self.buffer.flush
###         self.writable = self.buffer.writable
###         self.write = lambda s: self.buffer.write(s.encode("ascii"))
###         self.read = lambda: self.buffer.read().decode("ascii")
###         self.readline = lambda: self.buffer.readline().decode("ascii")
### 
### if sys.version_info[0] < 3:
###     sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
### else:
###     sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
### 
### def print(*args, **kwargs):
###     sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
###     at_start = True
###     for x in args:
###         if not at_start:
###             file.write(sep)
###         file.write(str(x))
###         at_start = False
###     file.write(kwargs.pop("end", "\n"))
###     if kwargs.pop("flush", False):
###         file.flush()
### 
### def inp():
###     return sys.stdin.readline().rstrip("\r\n")  # for fast input
### 
### def ii():
###     return int(inp())
### 
### def si():
###     return str(inp())
### 
### def li(lag = 0):
###     l = list(map(int, inp().split()))
###     if lag != 0:
###         for i in range(len(l)):
###             l[i] += lag
###     return l
### 
### def mi(lag = 0):
###     matrix = list()
###     for i in range(n):
###         matrix.append(li(lag))
###     return matrix
### 
### def lsi(): #string list
###     return list(map(str, inp().split()))
### 
### def printList(a, sep=" "):
###     print(sep.join(map(str, a)))
### # END Standard IO #

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

EVEN = 0
HILL = 1
VALLEY = 2

def main(f = None):
    init(f)
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]

        def solve():
            geo = [EVEN] * n
            count = 0
            for i in range(1, n-1):
                ai = arr[i-1]
                aj = arr[i]
                ak = arr[i+1]

                if ai < aj and aj > ak:
                    geo[i] = HILL
                    count += 1
                elif ai > aj and aj < ak:
                    geo[i] = VALLEY
                    count += 1
            if count == 0:
                return count

            decrease = 0
            for i in range(2, n-2):
                gi = geo[i-1]
                gj = geo[i]
                gk = geo[i+1]
                if gi > EVEN and gj > EVEN and gk > EVEN:
                    return count - 3
            for i in range(1, n-1):
                gi = geo[i]
                gj = geo[i+1]
                if gi == VALLEY and gj == HILL:
                    if arr[i-1] > arr[i+1]:
                        return count - 2
                elif gi == HILL and gj == VALLEY:
                    if arr[i-1] < arr[i+1]:
                        return count - 2

            return count - 1

        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()