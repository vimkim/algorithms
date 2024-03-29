import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

class DP:
    def __init__(s, arr):
        s.arr =arr
        s.n = len(arr)
        dp = [None] * s.n
        s.dp = dp
        for i in range(s.n):
            s.solve(i)

    def solve(s, lastIndex):
        x = lastIndex
        dp = s.dp
        a = s.arr
        val = dp[x]

        if x < 0:
            return 0
        if x < 2:
            return sum(a[:x+1])

        if val is not None:
            return val

        c2 = s.solve(x - 1) # not choose x
        c1 = s.solve(x - 2) + a[x] # not choose x-1
        c3 = s.solve(x - 3) + a[x] + a[x-1] # not choose x-2
        val = max(c1, c2 ,c3)
        dp[x] = val
        return val

def main(f = None):
    init(f)
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dp = DP(arr)
    ans = dp.solve(n-1)
    print(ans)



if __name__ == "__main__":
    main()