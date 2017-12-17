"""
Tests for the scripts that print output.
"""
import subprocess

cwd = "./docs/_static/02-introduction-to-python"  # TODO This means it can only be run from root dir
expected_out = b"15 15.0 True\n1275 1275.0 True\n"

def test_sum_of_integers_formula():
    out = subprocess.check_output(["python",
                                   "verify_sum_of_integers_formula.py"],
                                  cwd=cwd)
    assert out == expected_out
