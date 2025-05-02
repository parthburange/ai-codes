class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __repr__(self):
        return f"({self.jug1}, {self.jug2})"

def is_goal_state(state, goal):
    return state.jug1 == goal or state.jug2 == goal

def get_successors(state, capacity1, capacity2):
    return [
        State(capacity1, state.jug2),  # Fill jug1
        State(state.jug1, capacity2),  # Fill jug2
        State(0, state.jug2),          # Empty jug1
        State(state.jug1, 0),          # Empty jug2
        State(
            state.jug1 - min(state.jug1, capacity2 - state.jug2),
            state.jug2 + min(state.jug1, capacity2 - state.jug2)
        ),  # Pour jug1 to jug2
        State(
            state.jug1 + min(state.jug2, capacity1 - state.jug1),
            state.jug2 - min(state.jug2, capacity1 - state.jug1)
        )   # Pour jug2 to jug1
    ]

def dfs(capacity1, capacity2, goal):
    print("\nDFS Solution:")
    stack = [State(0, 0)]
    visited = set()

    while stack:
        current = stack.pop()

        if (current.jug1, current.jug2) in visited:
            continue

        visited.add((current.jug1, current.jug2))
        print(current)

        if is_goal_state(current, goal):
            print("Goal state reached!")
            return

        for next_state in get_successors(current, capacity1, capacity2):
            if (next_state.jug1, next_state.jug2) not in visited:
                stack.append(next_state)

    print("No solution found!")

if __name__ == "__main__":
    c1 = int(input("Enter capacity of jug1: "))
    c2 = int(input("Enter capacity of jug2: "))
    goal = int(input("Enter the goal amount: "))
    dfs(c1, c2, goal)
