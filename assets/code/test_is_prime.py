import is_prime

if is_prime.is_prime(23) is False:
    print("There is an error")

assert is_prime.is_prime(23) is True
assert is_prime.is_prime(4 * 7) is False
