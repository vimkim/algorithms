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



def main(f = None):
    init(f)
    N = int(input().strip())
    A = [int(i) for i in input().split()]
    last = [None for _ in range(N)]
    dp = [1 for _ in range(N)]
    dp[0] = 1
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if A[i] < A[j]:
                if dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
    print(max(dp))


if __name__ == "__main__":
    main()