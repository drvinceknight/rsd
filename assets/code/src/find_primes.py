import is_prime
import repeat_divide

def obtain_prime_factorisation(N):
    """
    Return the prime factorisation of a number.

    Inputs:
        - N: integer

    Outputs:
        - a list of prime factors
        - a list of the exponents of the prime factors
    """
    factors = []
    potential_factor = 1

    while N > 1:
        potential_factor += 1

        if is_prime.is_prime(potential_factor):

            N, exponent = repeat_divide.repeat_divide_number(N, potential_factor)

            if exponent > 0:
                factors.append((potential_factor, exponent))

    return factors

print(obtain_prime_factorisation(2 ** 3 * 11 * 23))
print(obtain_prime_factorisation(7))
