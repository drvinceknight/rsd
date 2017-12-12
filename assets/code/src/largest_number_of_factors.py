import prime_factors
counts = [len(prime_factors.get(n)) for n in range(1, 101)]
with open("../tex/largest_number_of_factors.tex", "w") as f:
     f.write(str(max(counts)))
