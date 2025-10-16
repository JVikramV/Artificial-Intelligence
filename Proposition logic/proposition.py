# Define truth values
truth_values = [True, False]

# Store models where KB is true
kb_models = []

# Evaluate the KB
for Q in truth_values:
    for P in truth_values:
        for R in truth_values:
            sentence1 = (not Q) or P         # Q → P
            sentence2 = (not P) or (not Q)   # P → ¬Q
            sentence3 = Q or R                # Q ∨ R

            kb_true = sentence1 and sentence2 and sentence3

            if kb_true:
                kb_models.append((Q, P, R))

# Initialize entailment flags
entails_R = True
entails_R_implies_P = True
entails_Q_implies_R = True

# Check entailments on models where KB is true
for (Q, P, R) in kb_models:
    # Check if R is true in all KB models
    if not R:
        entails_R = False

    # Check if R → P is true in all KB models
    if R and not P:
        entails_R_implies_P = False

    # Check if Q → R is true in all KB models
    if Q and not R:
        entails_Q_implies_R = False

# Output the results
print("Models where KB is true:")
for model in kb_models:
    print(f"Q={model[0]}, P={model[1]}, R={model[2]}")

print(f"\nDoes KB entail R? {entails_R}")
print(f"Does KB entail R → P? {entails_R_implies_P}")
print(f"Does KB entail Q → R? {entails_Q_implies_R}")
