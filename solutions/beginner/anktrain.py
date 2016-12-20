partners = (
    ('3UB', '6UB'),
    ('2MB', '5MB'),
    ('1LB', '4LB'),
    ('7SL', '8SU'),
)


def _partner(k):
    a = k % 8
    a = str(a) if a else '8'

    p = ''
    for l, m in partners:
        if a in l:
            p = m
            break
        if a in m:
            p = l
            break

    return str(k - (int(a) - int(p[0]))) + p[1:]


t = input()

for i in range(t):
    n = input()

    print _partner(n)
