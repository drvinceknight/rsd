import is_prime

if is_prime.check(23) is False:
    print("There is an error")

assert is_prime.check(23) is True
assert is_prime.check(4 * 7) is False
