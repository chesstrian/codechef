def array2str(k):
    k.reverse()

    return ''.join(map(str, k))


def multiply(a, k):
    result = []

    temp = 0
    for d in a:
        aux = d * k + temp
        result.append(aux % 10)
        temp = aux / 10

    while temp > 0:
        result.append(temp % 10)
        temp /= 10

    return result


def factorial(k):
    if k in (0, 1):
        return [1]
    else:
        return multiply(factorial(k - 1), k)


t = input()

for i in range(t):
    n = input()

    print array2str(factorial(n))
