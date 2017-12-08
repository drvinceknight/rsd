"""
Tests for the test_scatter_plot_of_prime_factors.py
"""
import subprocess
import os.path

expected_out = b'[(2, 3), (11, 1), (23, 1)]\n[(7, 1)]\n'
cwd = "./assets/code/src/"  # TODO This means it can only be run from root dir

def test_scatter_plot_of_prime_factors():
    out = subprocess.check_output(["python", "scatter_plot_of_prime_factors.py"], 
                                  cwd=cwd)
    # TODO: Best way to handle this? ( if __name__ ...?)
    # The import of `is_primes` (in this script) is still printing output.
    assert out == expected_out
    assert os.path.isfile(cwd + "scatter_plot_of_prime_factors.pdf")
