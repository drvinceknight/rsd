"""
Function to check if a number is prime.
"""

def check(N):
    """
    Test if N is prime.

    Inputs:
       - N: an integer

    Output:
       - A boolean
    """
    potential_factor = 1

    while potential_factor < N / 2:
        potential_factor = potential_factor + 1

        if (N % potential_factor == 0):
            return False
    return True
