import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())

def bfs(k):
    global visited, dq, ans, K, N
    if not 0 <= k <= 100000:
        return

    visited[k] = True
    dq.append((k, 0))

    while len(dq) > 0:
        curr, curStep = dq.popleft()
        if curr == N:
            ans = curStep
            return

        arr = [curr-1, curr+1]
        if curr % 2 == 0:
            arr.append(curr//2)
        for x in arr:
            if 0 <= x <= 100000 and not visited[x]:
                visited[x] = True
                dq.append((x, curStep + 1))


def main():
    global visited, dq, ans, K, N
    dq = collections.deque()
    K = 0
    N = 0
    ans = 0
    visited = [False for _ in range(100001)]
    N, K = (int(i) for i in input().split())
    bfs(K)
    print(ans)


if __name__ == "__main__":
    main()