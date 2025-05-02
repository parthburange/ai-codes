import heapq

# Directions: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state, goal, N):
    distance = 0
    for i in range(N):
        for j in range(N):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(goal.index(val), N)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def flatten(state):
    return [num for row in state for num in row]

def get_blank_pos(state, N):
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def swap_and_copy(state, i1, j1, i2, j2):
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def a_star(start, goal):
    N = len(start)
    start_flat = flatten(start)
    goal_flat = flatten(goal)

    start_tuple = tuple(start_flat)
    goal_tuple = tuple(goal_flat)

    frontier = []
    heapq.heappush(frontier, (0, 0, start, []))
    visited = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)
        current_flat = tuple(flatten(current))

        if current_flat in visited:
            continue
        visited.add(current_flat)

        if current_flat == goal_tuple:
            return path + [current]

        x, y = get_blank_pos(current, N)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                neighbor = swap_and_copy(current, x, y, nx, ny)
                h = manhattan_distance(neighbor, goal_flat, N)
                heapq.heappush(frontier, (g + 1 + h, g + 1, neighbor, path + [current]))

    return None

# ---------------- MAIN ----------------

if __name__ == "__main__":
    start = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]

    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    solution = a_star(start, goal)

    if solution:
        print("✅ Solution found in", len(solution) - 1, "moves:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print("-----")
    else:
        print(" No solution found.")
