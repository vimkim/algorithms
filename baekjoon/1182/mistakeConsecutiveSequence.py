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
    N, S = (int(i) for i in input().split())
    arr = [int(i) for i in input().split()]
    cum = [i for i in arr]
    for i in range(1, len(cum)):
        cum[i] += cum[i-1]

    print(arr)
    print(cum)
    count = 0
    if arr[0] == S:
        count += 1
    for i in range(N):
        for j in range(i+1, N):
            print(arr[i:j], sum(arr[i:j]))
            parSum = cum[j] - cum[i]
            print(parSum)
            if parSum == S:
                count += 1
    print(count)

if __name__ == "__main__":
    main()