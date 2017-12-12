import matplotlib.pyplot as plt
import prime_factors
xs = range(1, 101)
ys = [len(prime_factors.get(n)) for n in xs]
plt.scatter(xs, ys)
plt.savefig("scatter_plot_of_prime_factors.pdf")
