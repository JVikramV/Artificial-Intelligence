from collections import deque

# Goal state for the puzzle
GOAL_STATE = ((1,2,3),
              (4,5,6),
              (7,8,0))

# Moves for the empty tile (row_offset, col_offset)
MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return r, c

def swap_tiles(board, r1, c1, r2, c2):
    board_list = [list(row) for row in board]
    board_list[r1][c1], board_list[r2][c2] = board_list[r2][c2], board_list[r1][c1]
    return tuple(tuple(row) for row in board_list)

def get_children(board):
    r, c = find_zero(board)
    children = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_board = swap_tiles(board, r, c, nr, nc)
            children.append(new_board)
    return children

def DLS(state, goal, depth_limit, path, visited):
    if state == goal:
        return path
    if depth_limit <= 0:
        return None
    
    for child in get_children(state):
        if child not in visited:
            visited.add(child)
            result = DLS(child, goal, depth_limit - 1, path + [child], visited)
            if result is not None:
                return result
            visited.remove(child)
    return None

def IDDFS(start, goal, max_depth=30):
    for depth in range(max_depth):
        visited = set([start])
        result = DLS(start, goal, depth, [start], visited)
        if result is not None:
            return result
    return None

# Example start state (mixed up)
start_state = ((1,2,3),
               (4,0,6),
               (7,5,8))

solution_path = IDDFS(start_state, GOAL_STATE, max_depth=20)

if solution_path:
    print(f"Solution found in {len(solution_path)-1} moves:")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found within max depth.")
