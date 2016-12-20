def velocity(distance, time):
    return (distance * 3600) / (time * 1000.)


t = input()

for i in range(t):
    s, sg, fg, d, ti = map(int, raw_input().split())

    v = s + velocity(d * 50, ti)

    sebi = abs(sg - v)
    father = abs(fg - v)

    if sebi < father:
        print 'SEBI'
    elif father < sebi:
        print 'FATHER'
    else:
        print 'DRAW'
