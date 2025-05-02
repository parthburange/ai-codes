class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

# Function to check if the goal state is reached
def is_goal_state(state, goal):
    return state.jug1 == goal or state.jug2 == goal

# Function to print a state
def print_state(state):
    print(f"({state.jug1}, {state.jug2})")

# Depth First Search (DFS)
def dfs(capacity1, capacity2, goal):
    print("\nDFS Solution:")
    stack = []
    visited = [[False] * (capacity2 + 1) for _ in range(capacity1 + 1)]

    start = State(0, 0)
    stack.append(start)

    while stack:
        current = stack.pop()

        if visited[current.jug1][current.jug2]:
            continue

        visited[current.jug1][current.jug2] = True
        print_state(current)

        if is_goal_state(current, goal):
            print("Goal state reached!")
            return

        # Generate successors
        successors = [
            State(capacity1, current.jug2),  # Fill jug1
            State(current.jug1, capacity2),  # Fill jug2
            State(0, current.jug2),          # Empty jug1
            State(current.jug1, 0),          # Empty jug2
            State(current.jug1 - (capacity2 - current.jug2) if current.jug1 - (capacity2 - current.jug2) >= 0 else 0,
                   current.jug1 + current.jug2 if current.jug1 + current.jug2 <= capacity2 else capacity2),  # Pour jug1 to jug2
            State(current.jug1 + current.jug2 if current.jug1 + current.jug2 <= capacity1 else capacity1,
                   current.jug2 - (capacity1 - current.jug1) if current.jug2 - (capacity1 - current.jug1) >= 0 else 0)  # Pour jug2 to jug1
        ]

        # Push unvisited successors to stack
        for next_state in successors:
            if not visited[next_state.jug1][next_state.jug2]:
                stack.append(next_state)

    print("No solution found!")

# Breadth First Search (BFS)
def bfs(capacity1, capacity2, goal):
    print("\nBFS Solution:")
    queue = []
    visited = [[False] * (capacity2 + 1) for _ in range(capacity1 + 1)]

    start = State(0, 0)
    queue.append(start)

    while queue:
        current = queue.pop(0)

        if visited[current.jug1][current.jug2]:
            continue

        visited[current.jug1][current.jug2] = True
        print_state(current)

        if is_goal_state(current, goal):
            print("Goal state reached!")
            return

        # Generate successors
        successors = [
            State(capacity1, current.jug2),  # Fill jug1
            State(current.jug1, capacity2),  # Fill jug2
            State(0, current.jug2),          # Empty jug1
            State(current.jug1, 0),          # Empty jug2
            State(current.jug1 - (capacity2 - current.jug2) if current.jug1 - (capacity2 - current.jug2) >= 0 else 0,
                   current.jug1 + current.jug2 if current.jug1 + current.jug2 <= capacity2 else capacity2),  # Pour jug1 to jug2
            State(current.jug1 + current.jug2 if current.jug1 + current.jug2 <= capacity1 else capacity1,
                   current.jug2 - (capacity1 - current.jug1) if current.jug2 - (capacity1 - current.jug1) >= 0 else 0)  # Pour jug2 to jug1
        ]

        # Enqueue unvisited successors
        for next_state in successors:
            if not visited[next_state.jug1][next_state.jug2]:
                queue.append(next_state)

    print("No solution found!")

# Main function
def main():
    capacity1 = int(input("Enter capacity of jug1: "))
    capacity2 = int(input("Enter capacity of jug2: "))
    goal = int(input("Enter the goal amount: "))

    while True:
        print("\nMenu:")
        print("1. Solve using DFS")
        print("2. Solve using BFS")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            dfs(capacity1, capacity2, goal)
        elif choice == 2:
            bfs(capacity1, capacity2, goal)
        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
