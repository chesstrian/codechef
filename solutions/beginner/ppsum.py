def _sum(k):
    return k * (k + 1) / 2


t = input()

for i in range(t):
    d, n = map(int, raw_input().split())

    for j in range(d):
        n = _sum(n)

    print n
