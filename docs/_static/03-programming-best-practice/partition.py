def get_mean(a, b):
    """
    Find the mid point of two points

    Inputs:
        - a, b: floats

    Outputs:
        - the coordinate of the mid point: float
    """
    return (a + b) / 2

def get_mean_partition(a, b, number_of_partitions):
    """
    Compute the partition of [a, b] by using
    a uniform partitioning of
    number_of_partitions of [a, b]

    Inputs:
        - a, b: floats

    Outputs:
        - partition: list of the form [(left, right, midpoint)]
    """
    partition_size = (b - a) / number_of_partitions
    partition = []
    left, right = a, a + partition_size
    while left < b:
        partition.append((left, right, get_mean(left, right)))
        left, right = right, right + partition_size
    return partition
