class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []
        
    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)
    
    def add_rule(self, premise, conclusion):
        """Add a rule (premise -> conclusion) to the knowledge base."""
        self.rules.append((premise, conclusion))
    
    def forward_reason(self):
        """Perform forward reasoning to derive conclusions."""
        new_inferences = True
        while new_inferences:
            new_inferences = False
            for premise, conclusion in self.rules:
                if premise.issubset(self.facts) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    new_inferences = True

    def query(self, fact):
        """Check if a fact is in the knowledge base."""
        return fact in self.facts

# Initialize the knowledge base
kb = KnowledgeBase()

# Add facts to the knowledge base
kb.add_fact("Man(Marcus)")
kb.add_fact("Pompeian(Marcus)")

# Add rules (premise -> conclusion)
kb.add_rule({"Pompeian(Marcus)"}, "Roman(Marcus)")   # Pompeians are Romans
kb.add_rule({"Roman(Marcus)"}, "Loyal(Marcus)")      # Romans are Loyal
kb.add_rule({"Man(Marcus)"}, "Person(Marcus)")       # Men are Persons
kb.add_rule({"Person(Marcus)"}, "Mortal(Marcus)")    # Persons are Mortal

# Perform forward reasoning
kb.forward_reason()

# Query to check if Marcus is mortal
if kb.query("Mortal(Marcus)"):
    print("Marcus is mortal!")
else:
    print("Marcus is not mortal.")
