import find_primes

assert find_primes.obtain_prime_factorisation(2 ** 3 * 11 * 23) == [(2, 3),
                                                                    (11, 1),
                                                                    (23, 1)]
assert find_primes.obtain_prime_factorisation(1) == []
assert find_primes.obtain_prime_factorisation(7) == [(7, 1)]
