"""
Function to repeatedly divide a number by another number.
"""

def get_exponent_of_factor(N, b):
    """
    Count number of times b divides N.

    Inputs:
        - N: An int
        - b: A divisor

    Outputs:
        - The number of times that b divides N
    """
    count = 0
    while N >= b and N % b == 0:
        count += 1
        N = N / b
    return count
