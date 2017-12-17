import math

import integration
import partition as part

partition = part.get_mean_partition(0, math.pi, 5000)
value = integration.riemann_sum(func=math.sin, partition=partition)
assert abs(value - 2) < 10 ** (- 5)

partition = part.get_mean_partition(0, math.pi, 5000)
value = integration.riemann_sum(func=math.cos, partition=partition)
assert abs(value) < 10 ** (- 5)

value = integration.approximate_integral(math.sin, 0, math.pi, 5000)
assert abs(value - 2) < 10 ** (- 5)

value = integration.approximate_integral(math.cos, 0, math.pi, 5000)
assert abs(value) < 10 ** (- 5)
