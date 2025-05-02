import heapq

# Directions: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    heapq.heappush(open_set, (
                        g + 1 + heuristic(neighbor, goal),
                        g + 1,
                        neighbor,
                        path + [neighbor]
                    ))

    return None

# ---------------- STATIC ----------------

def main():
    # Hardcoded grid
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    # Hardcoded start and goal positions
    start = (0, 0)  # Start position (row, col)
    goal = (4, 4)   # Goal position (row, col)

    path = a_star_search(grid, start, goal)

    if path:
        print("\n Path found with", len(path) - 1, "moves:")
        for step in path:
            print(step)
    else:
        print("❌ No path found.")

if __name__ == "__main__":
    main()
