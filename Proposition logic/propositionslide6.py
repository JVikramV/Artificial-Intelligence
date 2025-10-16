# Define truth values
truth_values = [True, False]

# Store models where KB is true
kb_models = []

# Evaluate the KB
for A in truth_values:
    for B in truth_values:
        for C in truth_values:
            sentence1 = (A or C) and (B or (not C))          # Q → P
            sentence2 = A or B   # P → ¬Q
                            # Q ∨ R

            kb_true = sentence1 and sentence2 

            if kb_true:
                kb_models.append((A,B,C))

# Initialize entailment flags
entails_sentence2=True

# Check entailments on models where KB is true
for (A,B,C) in kb_models:
    # Check if R is true in all KB models
    if not sentence2:
       enatils_sentence2 = False

   
    

# Output the results
print("Models where KB is true:")
for model in kb_models:
    print(f"A={model[0]}, B={model[1]}, C={model[2]}")

print(f"\nDoes KB entail alpha? {entails_sentence2}")
