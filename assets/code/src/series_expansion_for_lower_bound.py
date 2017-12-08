import sympy as sym
n = sym.symbols('n')
series_expansion = sym.series(n / (sym.ln(n)), n, 1)
with open("../tex/series_expansion_for_lower_bound.tex", "w") as f:
    f.write(sym.latex(series_expansion))
