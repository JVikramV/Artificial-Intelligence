def is_variable(x):
    return isinstance(x, str) and x.islower()

def occurs_check(var, x, subst):
    if var == x:
        return True
    elif isinstance(x, tuple):
        return any(occurs_check(var, xi, subst) for xi in x)
    elif x in subst:
        return occurs_check(var, subst[x], subst)
    return False

def apply_subst(subst, term):
    if isinstance(term, tuple):
        return tuple(apply_subst(subst, t) for t in term)
    elif term in subst:
        return apply_subst(subst, subst[term])
    else:
        return term

def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = apply_subst(subst, x)
    y = apply_subst(subst, y)

    if x == y:
        return subst

    elif is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst

    elif is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst

    elif isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst

    else:
        return None
# P(f(x), g(y), y)
expr1 = ("P", ("f", "x"), ("g", "y"), "y")

# P(f(g(z)), g(f(a)), f(a))
expr2 = ("P", ("f", ("g", "z")), ("g", ("f", "a")), ("f", "a"))

# Run unification
mgu = unify(expr1, expr2)
print("Most General Unifier (MGU):", mgu)

