import random
import math

def generate_initial_state(n):
    """Generate a random initial state where each queen is placed in a different column."""
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_conflicts(state):
    """Calculate the number of conflicts (attacks) in the current state."""
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(state):
    """Generate all neighbors by moving one queen to a new row in its column."""
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if j != state[i]:
                neighbor = state[:]
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def acceptance_probability(old_conflicts, new_conflicts, temperature):
    """Calculate the probability of accepting a worse solution."""
    if new_conflicts < old_conflicts:
        return 1.0
    else:
        # Probability of accepting worse solution decreases with temperature
        return math.exp((old_conflicts - new_conflicts) / temperature)

def simulated_annealing(n, initial_temperature, cooling_rate):
    """Simulated Annealing algorithm to solve the N-Queens problem."""
    current_state = generate_initial_state(n)
    current_conflicts = calculate_conflicts(current_state)
    temperature = initial_temperature

    # Main loop
    while temperature > 1:
        # Generate neighbors and select one randomly
        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_conflicts = calculate_conflicts(next_state)

        # If the neighbor has fewer conflicts, move to it, or accept it based on probability
        if acceptance_probability(current_conflicts, next_conflicts, temperature) > random.random():
            current_state = next_state
            current_conflicts = next_conflicts

        # Cool down the temperature
        temperature *= cooling_rate

        # If solution is found (no conflicts)
        if current_conflicts == 0:
            return current_state

    return None  # Return None if no solution is found after cooling

def print_board(state):
    """Print the 4x4 chessboard."""
    n = len(state)
    for row in range(n):
        board_row = ['Q' if col == state[row] else '.' for col in range(n)]
        print(' '.join(board_row))
    print("\n")

# Test the algorithm for 4-Queens
n = 4
initial_temperature = 10000  # High initial temperature
cooling_rate = 0.95  # Cooling rate (0 < rate < 1)

solution = simulated_annealing(n, initial_temperature, cooling_rate)

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found.")
