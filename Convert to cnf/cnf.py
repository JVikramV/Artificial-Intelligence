from sympy import symbols, Or
from sympy.logic.boolalg import to_cnf

# Step 1: Define valid Boolean symbols
A = symbols('Animal_f1x', boolean=True)
B = symbols('Loves_x_f1x', boolean=True)
C = symbols('Loves_f2x_x', boolean=True)

# Step 2: Build logical expression (A ∨ B ∨ C)
expr = Or(A, B, C)

# Step 3: Convert to CNF (for completeness)
cnf_expr = to_cnf(expr, simplify=True)

# Step 4: Custom pretty print mapping back to original names
pretty_map = {
    A: "Animal(f1(x))",
    B: "Loves(x, f1(x))",
    C: "Loves(f2(x), x)"
}

def pretty(expr):
    text = str(expr)
    for sym, rep in pretty_map.items():
        text = text.replace(str(sym), rep)
    text = text.replace('|', ' ∨ ')  # Optional: nicer symbol
    text = text.replace('&', ' ∧ ')
    return text

print("CNF Formula:\n")
print(pretty(cnf_expr))