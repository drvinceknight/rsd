"""
Tests for number_of_factors_table.py
"""
import subprocess
import os.path

import pandas as pd

import find_primes

expected_out = b'[(2, 3), (11, 1), (23, 1)]\n[(7, 1)]\n'
cwd = "./assets/code/"  # TODO This means it can only be run from root dir

counts = [len(find_primes.obtain_prime_factorisation(n)) for n in range(95, 101)]
df = pd.DataFrame({"N": range(95, 101), "Number of factors": counts})
expected_table = df.to_latex(index=False)

def test_scatter_plot_of_prime_factors():
    out = subprocess.check_output(["python", "number_of_factors_table.py"],
                                  cwd=cwd + "src")

    assert out == expected_out

    with open(cwd + "tex/number_of_factors_table.tex", "r") as f:
        text = f.read()
    assert text == expected_table
