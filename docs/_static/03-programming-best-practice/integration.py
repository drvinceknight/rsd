import partition as part

def riemann_sum(func, partition):
    """
    Compute the Riemann sum for a given partition

    Inputs:
        - func: any single variable function
        - partition: list of the form [(left, right, midpoint)]

    Outputs:
        - a float
    """
    return sum(func(point) * (right - left) for left, right, point in partition)

def approximate_integral(func, a, b, number_of_partitions=1000):
    """
    Compute the approximate definite integral using Riemman integration over
    `number_of_partitions` partitions

    Inputs:
        - func: any single variable function
        - a, b: floats
        - number_of_partitions: int

    Outputs:
        - a float
    """
    partition = part.get_mean_partition(a=a, b=b,
                                        number_of_partitions=number_of_partitions)
    return riemann_sum(func, partition)
