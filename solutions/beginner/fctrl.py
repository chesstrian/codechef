def z(n):
    aux = 5

    result = 0
    while n / aux > 0:
        result += n / aux
        aux *= 5

    return result


t = input()

for i in range(t):
    k = input()

    print z(k)
