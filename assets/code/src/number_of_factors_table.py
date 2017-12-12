import pandas as pd
import prime_factors
counts = [len(prime_factors.get(n)) for n in range(95, 101)]
df = pd.DataFrame({"N": range(95, 101), "Number of factors": counts})
with open("../tex/number_of_factors_table.tex", "w") as f:
    f.write(df.to_latex(index=False))
