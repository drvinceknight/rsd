# Programming best practice

In this chapter we will consider a number of pillars of software development:

1. Modularisation;
2. Documentation;
3. Automated testing.

We will do this by writing software to find the prime factors of an integer.

## Basic scripting

Consider the file [`01-find_primes.py`]({{root}}/assets/code/01-find_primes.py).

Is it clear what this function is doing?

## Comments

Consider the file [`02-find_primes.py`]({{root}}/assets/code/02-find_primes.py).

Is this better?

Do all the comments explain what is happening?

## Better variable names

Consider the file [`03-find_primes.py`]({{root}}/assets/code/03-find_primes.py).

Using verbose/explicit variable names improves the code readability.

Note that now, some comments become useless: in fact some become "lies". Best
practice is to in fact comment code only when absolutely necessary and instead
rely on so called "self documented code".

## Modularity

Consider the 3 files:

- [`is_prime.py`]({{root}}/assets/code/is_prime.py)
- [`repeat_divide.py`]({{root}}/assets/code/repeat_divide.py)
- [`find_primes.py`]({{root}}/assets/code/find_primes.py)

Note here that we have broken each step of the algorithm in to it's own script
and further more we have documented each function using a specific documentation
as opposed to comments.

By breaking code in to little parts and clearly documenting (both through the
name of the function and appropriate use of comments) it becomes clearer what
each step does and also ensures that comments do not become lies.

## Testing

Open the 3 files:

- [`test_is_prime.py`]({{root}}/assets/code/test_is_prime.py)
- [`test_repeat_divide.py`]({{root}}/assets/code/test_repeat_divide.py)
- [`test_find_primes.py`]({{root}}/assets/code/test_find_primes.py)

These files include code to ensure that our code does what it is expected to do.

In `test_is_prime.py` we see using a simple `if` statement that would check if
if the code is incorrect but from then on we use a Python statement called
`assert` which does this in a simpler way. Most languages have something
similar.

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
- Testing: write a test for your code. This ensures that you know your code does
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
