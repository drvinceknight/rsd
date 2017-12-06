"""
Function to repeatedly divide a number by another number.
"""

def repeat_divide_number(N, b):
    """
    Divide N by b until b no longer divide N

    Inputs:
        - N: An int
        - b: A divisor

    Outputs:
        - The result of repeatedly integer dividing N by b
        - The number of times that b divides N
    """
    count = 0
    while N >= b and N % b == 0:
        count += 1
        N = N / b
    return int(N), count
