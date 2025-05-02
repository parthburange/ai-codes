N = 3  # 3x3 puzzle

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank space
]

def calculate_misplaced_tiles(puzzle):
    misplaced = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] != 0 and puzzle[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced

def find_blank(puzzle):
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 0:
                return i, j

def copy_puzzle(puzzle):
    return [row[:] for row in puzzle]

def print_puzzle(puzzle):
    for row in puzzle:
        for val in row:
            print("   " if val == 0 else f"{val:2d} ", end="")
        print()
    print()

# Possible moves: down, up, right, left
moves = [
    (1, 0),   # Down
    (-1, 0),  # Up
    (0, 1),   # Right
    (0, -1)   # Left
]

def hill_climbing(puzzle):
    current = copy_puzzle(puzzle)
    move_count = 0

    while True:
        blank_row, blank_col = find_blank(current)
        current_heuristic = calculate_misplaced_tiles(current)
        best_heuristic = current_heuristic
        best_move_index = -1
        best_puzzle = None

        for i, (dr, dc) in enumerate(moves):
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                new_puzzle = copy_puzzle(current)
                new_puzzle[blank_row][blank_col], new_puzzle[new_row][new_col] = \
                    new_puzzle[new_row][new_col], new_puzzle[blank_row][blank_col]
                new_heuristic = calculate_misplaced_tiles(new_puzzle)

                if new_heuristic < best_heuristic:
                    best_heuristic = new_heuristic
                    best_move_index = i
                    best_puzzle = new_puzzle

        if best_move_index == -1:
            print("Local Optima Reached! No better move found.")
            print(f"Total moves taken: {move_count}")
            break

        current = best_puzzle
        move_count += 1
        print(f"Move {move_count}:")
        print_puzzle(current)

        if best_heuristic == 0:
            print("Goal State Reached!")
            print(f"Total moves taken: {move_count}")
            break

def get_user_input():
    print("Enter the 3x3 puzzle row by row (use 0 for the blank):")
    puzzle = []
    for i in range(N):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != N:
                    raise ValueError
                puzzle.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter exactly 3 integers separated by spaces.")
    return puzzle

# Main execution
if __name__ == "__main__":
    puzzle = get_user_input()
    print("\nInitial State:")
    print_puzzle(puzzle)

    print("Solving using Hill Climbing with Misplaced Tile Heuristic...\n")
    hill_climbing(puzzle)
