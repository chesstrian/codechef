x, y = raw_input().split()

x = int(x)
y = float(y)

if x % 5 or x + 0.5 > y:
    print "%.2f" % y
else:
    print "%.2f" % (y - x - 0.5)
