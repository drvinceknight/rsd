import pandas as pd
import find_primes
counts = [len(find_primes.obtain_prime_factorisation(n)) for n in range(95, 101)]
df = pd.DataFrame({"N": range(95, 101), "Number of factors": counts})
with open("../tex/number_of_factors_table.tex", "w") as f:
    f.write(df.to_latex(index=False))
