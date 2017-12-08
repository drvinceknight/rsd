"""
Tests for the series_expansion_for_lower_bound.py
"""
import subprocess
import os.path

import sympy as sym

cwd = "./assets/code/"  # TODO This means it can only be run from root dir
n = sym.symbols('n')
out = sym.latex(sym.series(n / (sym.ln(n)), n, 1))

def test_scatter_plot_of_prime_factors():
    subprocess.call(["python", "series_expansion_for_lower_bound.py"],
                                  cwd=cwd + "src")

    with open(cwd + "tex/series_expansion_for_lower_bound.tex", "r") as f:
        text = f.read()
    assert text == out
