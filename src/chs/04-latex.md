# LaTeX

LaTeX is the main package used in Mathematics for preparing documents (thesis,
articles etc).

## Creating a simple document

Open a new file in your editor and write the following:

```tex
\documentclass{article}

\begin{document}
    Hello
\end{document}
```

Save this file (in `rsd-workshop`) as `main.tex`.

Now open your command line and navigate to `rsd-workshop` and run the following
command:

```bash
pdflatex main.tex
```

This will create a pdf file `main.pdf` (and a number of auxiliary files).

## Calling one document from another

In [Chapter 01](../01/) we created a sub directory called `tex`. In that
directory create a new LaTeX file called `chapter-01.tex`:

```tex
Let us investigate the number of prime factors of integers.
```

Now modify `main.tex` to be:

```tex
\documentclass{article}

\title{The number of prime factors}

\begin{document}
    \maketitle
    \input{tex/chapter-01.tex}
\end{document}
```

Now "compile" `main.tex:

```bash
pdflatex main.tex
```

This `input` command allows us to keep our directory structure clean and
organised.

## Directory structure

In general keeping a directory structure clear and well structured is helpful.
The following suggested structure is one of many possible ways of doing things.

Let us move all the previously written python files to the `src` (source)
directory.

Thus, our directory should look like this:

```
|--- rsd
     main.tex
     main.pdf
     main.*
     |--- tex
          |--- chapter-01.tex
     |--- src
          |--- find_primes_v1.py
          |--- find_primes_v2.py
          |--- find_primes_v3.py
          |--- find_primes.py
          |--- is_prime.py
          |--- repeat_divide.py
          |--- test_find_primes.py
          |--- test_is_prime.py
          |--- test_repeat_divide.py

```

Let us write another script that counts **and** plots the number of prime
factors for all integers less than 100. In `src` create
[`scatter_plot_of_prime_factors.py`]({{root}}/assets/code/src/scatter_plot_of_prime_factors.py)
(note: the name of the file).

**Note** When we run that file, the `print` statements of the file it "imports"
are run. We can remove them.

Now let us include this plot in our `chapter-01.tex`:


```tex
Let us investigate the number of prime factors of integers.

Figure~\ref{fig:scatter_plot_of_prime_factors} shows the number of prime
factors for each integer less than 100.

\begin{center}
    \begin{figure}[!hbtp]
        \includegraphics[width=5cm]{src/scatter_plot_of_prime_factors.pdf}
        \caption{The number of prime factors of each integer}
        \label{scatter_plot_of_prime_factors}
    \end{figure}
\end{center}
```

**Note** when we do this we need to include `\include{graphicx}` in the preamble
of `main.tex`.

## Including research output in LaTeX

If you have research output created from software:

- Specific measures (counting something)
- Complex equations
- Data tables

It is possible to make errors when writing these by hand (not relevant to the
case of images of course) to your LaTeX document. Best practice is to output
these from your software directly to a file that will be included.

### Directly including text.

For example, let us write a python script to get the number with the most prime
factors. In `src` create:
[`largest_number_of_factors.py`]({{root}}/assets/code/src/largest_number_of_factors.py).

This file creates `tex/largest_number_of_factors.tex`.
We then can include the output directly in to `chapter-01.tex`:

```tex
Let us investigate the number of prime factors of integers.

Figure~\ref{fig:scatter_plot_of_prime_factors} shows the number of prime
factors for each integer less than 100.

\begin{center}
    \begin{figure}[!hbtp]
        \includegraphics[width=5cm]{src/scatter_plot_of_prime_factors.pdf}
        \caption{The number of prime factors of each integer}
        \label{scatter_plot_of_prime_factors}
    \end{figure}
\end{center}

The number with the most prime factors
has\input{tex/largest_number_of_factors} prime factors.
```

### Including complex equations

At times, a computer algebra system might be used to manipulate an expression,
in this case it could be worth outputting the output directly to file and
reading it in. (Again, avoiding the opportunity for human error).

Let us write a python script to generate the series expansion for the first 3
terms of the lower bound of the number of primes less than $n$:

$$
\frac{n}{\log{n}}
$$

Create
[`series_expansion_for_lower_bound.py`]({{root}}/assets/code/src/series_expansion_for_lower_bound.py)
we will use the
Python library Sympy (for symbolic mathematics) that also has the ability to
generate LaTeX directly from it's output (similar capabilities exist in other
computer algebra systems).

This creates `tex/series_expansion_for_lower_bound.tex`.
Now let us modify the `chapter-01.tex` to include this:

```tex
Let us investigate the number of prime factors of integers.

Figure~\ref{fig:scatter_plot_of_prime_factors} shows the number of prime
factors for each integer less than 100.

\begin{center}
    \begin{figure}[!hbtp]
        \includegraphics[width=5cm]{src/scatter_plot_of_prime_factors.pdf}
        \caption{The number of prime factors of each integer}
        \label{scatter_plot_of_prime_factors}
    \end{figure}
\end{center}

The number with the most prime factors
has \input{tex/largest_number_of_factors}prime factors.

The number of factors is probably related to the number of primes which has
a lower bound given by:

\small
\[
\pi(n)=\frac{n}{\log{n}}=\input{tex/series_expansion_for_lower_bound.tex}
\]

```

### Including tables

Finally, you might similarly have generated some data that you'd like to include
in the form of a table.

To avoid human error we can generate the LaTeX code for a table directly in
code.

With python we will do this with a library called pandas (which implements a
dataframe similar to R). Similar capabilities exist in other languages or the
table code could be generated directly.

Let us write
[`number_of_factors_table.py`]({{root}}/assets/code/src/number_of_factors_table.py).
This creates `tex/number_of_factors_table.tex`.
Let us include this in the LaTeX document:

```tex
Let us investigate the number of prime factors of integers.

Figure~\ref{fig:scatter_plot_of_prime_factors} shows the number of prime
factors for each integer less than 100.

\begin{center}
    \begin{figure}[!hbtp]
        \includegraphics[width=5cm]{src/scatter_plot_of_prime_factors.pdf}
        \caption{The number of prime factors of each integer}
        \label{scatter_plot_of_prime_factors}
    \end{figure}
\end{center}

Table~\ref{tab:number_of_factors_table} shows these counts for \(95\leq
n\leq 100\).

\begin{center}
    \begin{table}[!hbtp]
        \input{tex/number_of_factors_table.tex}
    \end{table}
\end{center}

The number with the most prime factors
has\input{tex/largest_number_of_factors} prime factors.

The number of factors is probably related to the number of primes which has
a lower bound given by:

\[
\pi(n)=\frac{n}{\log{n}}=\input{tex/series_expansion_for_lower_bound.tex}
\]
```

**Note** when we do this we need to include `\include{booktabs}` in the preamble
of `main.tex`.

## Summary

A lot of the principles to writing good software apply to writing good LaTeX.
The particular choice of directory structure suggested here is in not a hard
rule but it allows for a consistent approach that you can use on a number of
projects.

## Tip

Try to line break your LaTeX source code: a paragraph in the rendered pdf
corresponds to a text separated by a blank line in the source. The reason for
this will become clear in the next chapter.

## Exercise

1. Use the following code that counts how many numbers all equally have the most
   factors:
   [count_maxima_for_number_of_primes.py]({{root}}/assets/code/src/count_maxima_for_number_of_primes.py)
2. Modify all previous code to repeat the analysis for numbers between 1 and
   250.
