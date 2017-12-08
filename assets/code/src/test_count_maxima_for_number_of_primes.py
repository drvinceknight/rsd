"""
Tests for the largest_number_of_factors.py
"""
import subprocess
import os.path

expected_out = b'[(2, 3), (11, 1), (23, 1)]\n[(7, 1)]\n'
cwd = "./assets/code/"  # TODO This means it can only be run from root dir

def test_scatter_plot_of_prime_factors():
    out = subprocess.check_output(["python",
                                   "count_maxima_for_number_of_primes.py"],
                                  cwd=cwd + "src")
    # TODO: Best way to handle this? ( if __name__ ...?)
    # The import of `is_primes` (in this script) is still printing output.
    assert out == expected_out

    with open(cwd + "tex/count_maxima_for_number_of_primes.tex", "r") as f:
        text = f.read()
    assert text == '8'
