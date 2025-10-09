import random

def generate_initial_state(n):
    """Generate a random initial state where each queen is placed in a different column."""
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_conflicts(state):
    """Calculate the number of conflicts in the current state."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are in the same diagonal
            if abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(state):
    """Generate all possible neighbors by moving one queen to a new row in its column."""
    neighbors = []
    for i in range(len(state)):
        # Try moving the queen in each column to a new row (except the current row)
        for j in range(len(state)):
            if j != state[i]:  # Don't move the queen to the same row
                new_state = state[:]
                new_state[i] = j
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n):
    """Hill climbing algorithm for solving N-Queens problem."""
    current_state = generate_initial_state(n)
    current_conflicts = calculate_conflicts(current_state)

    while current_conflicts > 0:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_conflicts = current_conflicts

        # Select the best neighbor (with fewer conflicts)
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_state = neighbor
                next_conflicts = neighbor_conflicts

        # If no better neighbor found, we are stuck in a local minimum
        if next_conflicts >= current_conflicts:
            return None  # No solution found, or stuck in a local minimum

        # Move to the best neighbor
        current_state = next_state
        current_conflicts = next_conflicts
        print("Current State:", current_state, "Conflicts:", current_conflicts)

    return current_state

def print_board(state):
    """Print the chessboard with the queens placed."""
    n = len(state)
    for i in range(n):
        row = ['Q' if j == state[i] else '.' for j in range(n)]
        print(' '.join(row))
    print("\n")

# Test the algorithm
n = 4 # Size of the board (8-Queens)
solution = hill_climbing(n)
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found.")
