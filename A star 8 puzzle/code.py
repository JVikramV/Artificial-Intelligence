import heapq

# Define the goal state for the 8-puzzle
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define the possible moves (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row_change, col_change)

# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        value = state[i]
        if value == 0:
            continue
        target_row, target_col = (value - 1) // 3, (value - 1) % 3
        current_row, current_col = i // 3, i % 3
        distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

# Define the A* search algorithm
def astar_search(start_state):
    start_state = tuple(start_state)  # Make the start state a tuple
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, None))
    came_from = {}
    g_score = {start_state: 0}
    
    while open_list:
        _, current_cost, current_state, parent_state = heapq.heappop(open_list)
        
        if current_state == GOAL_STATE:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = came_from.get(current_state, None)
            return path[::-1]  # Return reversed path (from start to goal)
        
        zero_index = current_state.index(0)
        zero_row, zero_col = zero_index // 3, zero_index % 3
        
        for move in MOVES:
            new_row, new_col = zero_row + move[0], zero_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(current_state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = tuple(new_state)
                
                tentative_g_score = current_cost + 1
                if new_state not in g_score or tentative_g_score < g_score[new_state]:
                    g_score[new_state] = tentative_g_score
                    f_score = tentative_g_score + manhattan_distance(new_state)
                    heapq.heappush(open_list, (f_score, tentative_g_score, new_state, current_state))
                    came_from[new_state] = current_state
    
    return None  # No solution found

# Function to print the puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

# Example usage:
start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Goal state (just for illustration, can be any state)
goal_state = astar_search(start_state)

if goal_state:
    print("Solution found!")
    for state in goal_state:
        print_state(state)
        print()
else:
    print("No solution exists.")
