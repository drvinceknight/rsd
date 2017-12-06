def prime_factorisation(N):
    factors = []  # Create empty lists for factors
    exponents = []  # Create empty list for exponnts
    potential_factor = 1  # Start with the potential factor
    while N > 1:  # Check all numbers until N
        potential_factor += 1
        potential_factor_factors = 1
        prime = True
        # Check if number is prime
        while potential_factor_factors < potential_factor - 1:  # For some reason need to go to potential
            potential_factor_factors += 1
            prime = prime and (potential_factor % potential_factor_factors != 0)
        if prime:  # If prime
            count = 0
            while N >= potential_factor and N % potential_factor == 0:
                count += 1
                N = int(N / potential_factor)
            if count > 0:
                factors.append(potential_factor)
                exponents.append(count)
    return factors, exponents

print(prime_factorisation(2 ** 3 * 11 * 23))
print(prime_factorisation(7))
