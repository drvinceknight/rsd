import prime_factors

assert prime_factors.get(2 ** 3 * 11 * 23) == [(2, 3), (11, 1), (23, 1)]
assert prime_factors.get(1) == []
assert prime_factors.get(7) == [(7, 1)]
