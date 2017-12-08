import matplotlib.pyplot as plt
import find_primes
xs = range(1, 101)
ys = [len(find_primes.obtain_prime_factorisation(n)) for n in xs]
plt.scatter(xs, ys)
plt.savefig("scatter_plot_of_prime_factors.pdf")
