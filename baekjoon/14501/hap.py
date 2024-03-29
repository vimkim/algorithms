import sys
import os


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


if len(sys.argv) == 1:
    if os.path.isfile("in/i"):
        setStdin("in/i")
    elif os.path.isfile("i"):
        setStdin("i")
elif len(sys.argv) == 2:
    setStdin(sys.argv[1])
else:
    assert False, "Too many sys.argv: %d" % len(sys.argv)


def solution(t, p):
    dp = p[:]

    for i in range(n):
        for j in range(i + t[i], n):
            dp[j] = max(dp[j], dp[i] + p[j])
    # dp 생성 완료 후, T(상담이 걸리는 기간) 을 따져서, 조건을 만족시키는 가장 큰 수를 반환하고자 함
    return max(dp)


n = int(input())
t = []
p = []
for i in range(n):
    #consult.append(list(map(int,input().split())))
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
#print(solution(consult))
p = [p[i] if t[i] + i <= n else 0 for i in range(n)]
print(solution(t, p))