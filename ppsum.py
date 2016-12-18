import sys

t = int(sys.stdin.readline())


def _sum(k):
    return k * (k + 1) / 2


for i in range(t):
    d, n = map(int, sys.stdin.readline().split(' '))

    for j in range(d):
        n = _sum(n)

    print n
