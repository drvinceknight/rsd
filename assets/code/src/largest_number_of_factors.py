import find_primes
counts = [len(find_primes.obtain_prime_factorisation(n)) for n in range(1, 101)]
with open("../tex/largest_number_of_factors.tex", "w") as f:
     f.write(str(max(counts)))
