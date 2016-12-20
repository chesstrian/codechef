def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


t = input()

for i in range(t):
    n = input()
    s = map(int, raw_input().split())

    min_lcm = 10 ** 19

    for j in enumerate(s[:-1], start=1):
        index, value = j
        for k in s[index:]:
            min_lcm = min(lcm(value, k), min_lcm)

    print min_lcm
