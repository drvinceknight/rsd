def primes(N):
    f = []
    e = []
    i = 1
    while N > 1:
        i = i + 1
        k = 1
        check = True

        while k < i - 1:
            k = k + 1
            check = check and (i % k != 0)
        if check:
            c = 0
            while N >= 1 and N % i == 0:
                c = c + 1
                N = N / i
            if c > 0:
                f.append(i)
                e.append(c)
    return f, e

print(primes(2 ** 3 * 11 * 23))
print(primes(7))
