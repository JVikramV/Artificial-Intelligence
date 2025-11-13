# Simple proof-by-resolution for "John likes peanuts"

# Clauses in CNF (as sets of literals)
KB = [
    {"~Eats(Anil,Peanuts)", "~Alive(Anil)", "Food(Peanuts)"},
    {"Eats(Anil,Peanuts)"},
    {"Alive(Anil)"},
    {"~Food(Peanuts)", "Likes(John,Peanuts)"},  # John likes all food instantiated for Peanuts
]

Goal = "Likes(John,Peanuts)"


# Helper function: Resolve two clauses
def resolve(c1, c2):
    resolvents = []
    for literal in c1:
        neg_literal = "~" + literal if literal[0] != "~" else literal[1:]
        if neg_literal in c2:
            new_clause = (c1 - {literal}) | (c2 - {neg_literal})
            resolvents.append(new_clause)
    return resolvents

# Negate goal and add to KB
negated_goal = "~" + Goal
KB.append({negated_goal})

# Resolution loop
new_clauses = set()
proved = False

while True:
    n = len(KB)
    pairs = [(KB[i], KB[j]) for i in range(n) for j in range(i+1, n)]
    added = False

    for c1, c2 in pairs:
        for resolvent in resolve(c1, c2):
            if len(resolvent) == 0:
                proved = True
                break
            if resolvent not in KB:
                KB.append(resolvent)
                added = True
        if proved:
            break
    if proved:
        print("Goal Proven:", Goal)
        break
    if not added:
        print("Cannot prove the Goal.")
        break
