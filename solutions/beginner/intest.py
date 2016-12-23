n, k = map(int, raw_input().split())

counter = 0
for i in range(n):
    ti = input()
    if not ti % k:
        counter += 1

print counter
