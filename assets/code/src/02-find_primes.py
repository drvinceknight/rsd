def pfact(N):
    f = []  # Create empty lists for factors
    i = 1  # Start with the potential factor
    while N > 1:  # Check all numbers until N
        i = i + 1  # add 1 to i
        k = 1  # Set count to check if I is prime
        check = True
        # Check if number is prime
        while k < i - 1:  # For some reason need to go to potential
            k = k + 1
            check = check and (i % k != 0)
        if check:  # If prime
            c = 0  # Setting c to 0
            while N >= 1 and N % i == 0:  # Repeating
                c = c + 1  # Add 1 to c
                N = N / i  # Divide M by factor
            if c > 0:
                f.append((i, c))
    return f

print(pfact(2 ** 3 * 11 * 23))
print(pfact(7))
