# Programming best practice

In this chapter we will consider a number of pillars of software development:

1. Modularisation;
2. Documentation;
3. Automated testing.

We will do this by writing software to find the prime factors of an integer.

## Discussion

Before looking any further there will be a class discussion.

## Files from discussion

- [`find_primes_v1.py`]({{root}}/assets/code/src/find_primes_v1.py).
- [`find_primes_v2.py`]({{root}}/assets/code/src/find_primes_v2.py).
- [`find_primes_v3.py`]({{root}}/assets/code/src/find_primes_v3.py).
- [`is_prime.py`]({{root}}/assets/code/src/is_prime.py)
- [`integer_division`]({{root}}/assets/code/src/integer_division.py)
- [`prime_factors.py`]({{root}}/assets/code/src/prime_factors.py)
- [`test_is_prime.py`]({{root}}/assets/code/src/test_is_prime.py)
- [`test_integer_division.py`]({{root}}/assets/code/src/test_integer_division.py)
- [`test_prime_factors.py`]({{root}}/assets/code/src/test_prime_factors.py)

## Code convention

If you look through the code carefully above you will see that the style is
consistent across each file:

- Variable and function names all use "snake case" (as opposed to for example
  "camel case": `IsPrime`).
- There are less than 80 characters in every line.
- The documentation follows a consistent style: listing "Inputs" and "Outputs".

This is important. A consistent style convention
makes readability of the code easier.

The actual style convention used is not important, just that a given convention
is used.

Most languages have an accepted convention:

- Python has [PEP8](https://www.python.org/dev/peps/pep-0008/)
- C++ has a few but [Bjarne
  Stroustrup's](http://www.stroustrup.com/bs_faq2.html) is popular.o
- Java also has a few, here is [Google's
  one](https://google.github.io/styleguide/javaguide.html).

Be sure to use a given convention and aim to stick to it. Your editor almost
certainly has a plugin or similar that checks the style for you. Don't be
afraid to break a given rule it it makes sense to do so: these are all meant to
e helpful and not constraining.

## Summary

There are three aspects to writing good software:

- Modularity: break code in to small components that are meaningful and easier
  to debug.
- Documentation: document your code. Do this by choosing verbose and meaningful
  variable and function names but also by writing a "manual" for each part of
  your code.
- Testing: write tests for your code. This ensures that you know your code does
  what it's supposed to do. It will also prove invaluable when it comes to
  debugging as you can immediately find out which part of your code doesn't
  work.

These 3 things are all as important as each and good software requires all
three. You might well have more fun working on a particular aspect of it but do
not prioritise any one area over another.

# Tip

One approach to writing good code is to start by writing the test and then work
backwards by writing the function to make the test pass:

1. This ensures your test fails (and isn't passing coincidentally).
2. This often helps conceptualise what you want your function to do.

# Optional

Using the discussed principles implement a function to carry out Riemann
integration over a closed interval $[a, b]$ for any given ordered partitioning
of $[a, b]$:

$$
\int_{a}^{b}f(x)dx \approx \sum_{k=1}^{n}f(t_k)(x_k - x_{k - 1})
$$

where $t_k$ is some point representative of the $k$th partition of $[a, b]$
given by points $x_k, x_{k-1}$.
