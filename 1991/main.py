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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def main(f = None):
    init(f)
    pass
    N = int(input().strip())
    import string
    abc = string.ascii_uppercase[:N]
    loc = {c:None for c in abc}
    for c in abc:
        loc[c] = Node(c)

    for _ in range(N):
        p, l, r = input().split()
        
    
    root = loc['A']



if __name__ == "__main__":
    main()
