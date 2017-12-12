# Introduction to Python

The programming language we will use in this course is Python.

Python is a popular language in industry and research with a number of libraries
very useful for mathematics:

- Symbolic mathematics with `sympy`
- Numerical mathematics with `numpy`
- Machine learning with `sklearn`
- Data analysis with `pandas`

In this chapter we will go over some basic Python.

## Using the Python interpreter

Open your command line and type:

```bash
python
```

This will start a prompt that looks something like:

```bash

Python 3.5.2 |Anaconda custom (64-bit)| (default, Jul  2 2016, 17:53:06) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

The `>>>` indicates point at which you can type python code.

Type `2 + 2` and press enter. You can see what this looks like below:

```python
>>> 2 + 2
4

```

## Creating numeric variables

We can assign variables to values using the `=` operator:

```python
>>> the_meaning_of_life = 42
>>> the_meaning_of_life = the_meaning_of_life + 2
>>> the_meaning_of_life
44

```

## Creating boolean variables

We can create boolean values using a number of comparison operators which
include:

- `==` equals
- `!=` not equals
- `>` strictly greater
- `>=` greater than or equal

```python
>>> is_42 = the_meaning_of_life == 42
>>> is_42
False
>>> greater_than_42 = the_meaning_of_life > 42
>>> greater_than_42
True

```

## Creating list variables

Python has an indexable structure called lists:

```python
>>> numbers = [1, 2, 4, 5]
>>> max(numbers)
5
>>> min(numbers)
1
>>> sum(numbers)
12
>>> numbers[0]
1
>>> numbers[-2]
4
>>> numbers.append(50)
>>> numbers
[1, 2, 4, 5, 50]

```

## Using Python scripts

To start to write more sophisticated code (software) we can write code
inside a file which we can then run using the command line.

### Writing a python script

Open one of the recommended text editors and create a new file in the
`rsd-workshop` (created in [Chapter 01](../01/)) save it as `01-hello-world.py`.
Inside the file write the following (ignore the `>>>`):

```python
print("hello world")
```

### Running a python script

Using the command line, let us now "run" this file using the command line:

```bash
python 01-hello-world.py
```

You can in fact run various programming languages this way: saving them to a
file in your editor of choice and running them with the correct command.

This allows for flexibility as you can choose an editor that has features you
enjoy and customise it to work for you.

## If statements

We can use boolean variables to create logical statements.

Write a file called `02-if-statements.py`, include the following code and run
it.

```python
N = 572
if N % 2 == 0:
    print("N is even")
else:
    print("N is odd")

```

**Note** white space and indentation is important in python. The indented code
block indicate what code to execute if the boolean variable `N % 2 == 0` is
`True`.

## While loops

It is possible to repeat code using `while` loops which will repeatedly check a
boolean variable.

Write a file called `03-while-loops.py`, include the following code and run
it.

```python
N = 0
even_number_count = 0
while N < 10:
    if N % 2 == 0:
        even_number_count = even_number_count + 1
    N = N + 1
print(even_number_count)

```

## Functions

It is possible to create functions in python which we will use later to write
modular code.

Write a file called `04-functions.py`, include the following code and run it.

```python
def count_even_numbers(upper_limit):
    N = 0
    even_number_count = 0
    while N < upper_limit:
        if N % 2 == 0:
            even_number_count = even_number_count + 1
        N = N + 1
    return even_number_count
print(count_even_numbers(10))
print(count_even_numbers(42))


```

# Tip

Explore your editor: both Atom and VS Code offer many plugins for Python. This
is not just a luxury to make things easier but **also** helps avoid mistakes by
letting the plugins check various things for you.

This is not just the case for these editors and Python. Most good editors have a
full ecosystem of tools available to support the writing of code in many
languages.

# Exercise

Write some code to compute and compare both sides of the following equation, for
varying values of $N$.

$$
\sum_{i=1}^Ni=\frac{N(N+1)}{2}
$$
