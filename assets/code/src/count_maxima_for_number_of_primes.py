import find_primes
counts = [len(find_primes.obtain_prime_factorisation(n)) for n in range(1, 101)]
number_of_maxima = counts.count(max(counts))
with open("../tex/count_maxima_for_number_of_primes.tex", "w") as f:
     f.write(str(number_of_maxima))
