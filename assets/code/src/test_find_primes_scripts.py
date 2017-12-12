"""
Tests for the scripts that print output.
"""
import subprocess

expected_out = b'[(2, 3), (11, 1), (23, 1)]\n[(7, 1)]\n'
cwd = "./assets/code/src/"  # TODO This means it can only be run from root dir

def test_01_find_primes():
    out = subprocess.check_output(["python", "find_primes_v1.py"],
                                  cwd=cwd)
    assert out == expected_out

def test_02_find_primes():
    out = subprocess.check_output(["python", "find_primes_v2.py"],
                                  cwd=cwd)
    assert out == expected_out

def test_03_find_primes():
    out = subprocess.check_output(["python", "find_primes_v3.py"],
                                  cwd=cwd)
    assert out == expected_out
