import is_prime
import integer_division

def get(N):
    """
    Return the prime factorisation of a number.

    Inputs:
        - N: integer

    Outputs:
        - a list of 2-tuples of the prime factor and its exponent
    """
    factors = []
    potential_factor = 1

    while N > 1:
        potential_factor += 1

        if is_prime.check(potential_factor):

            exponent = integer_division.get_exponent_of_factor(N, potential_factor)
            N = (N / (potential_factor ** exponent))

            if exponent > 0:
                factors.append((potential_factor, exponent))

    return factors

print(get(2 ** 3 * 11 * 23))
print(get(7))
