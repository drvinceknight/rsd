import partition

assert partition.get_mean(2, 5) == 3.5
assert partition.get_mean(0, 0) == 0

assert partition.get_mean_partition(0, 1, 2) == [(0, .5, .25), (.5, 1, .75)]
