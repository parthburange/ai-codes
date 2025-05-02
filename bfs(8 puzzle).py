from copy import deepcopy
from collections import deque

N = 3  # Size of the puzzle (3x3)

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Moves: Left, Right, Up, Down
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# Class to represent a state of the puzzle
class Node:
    def __init__(self, puzzle, x, y, newX, newY, depth, parent):
        self.puzzle = deepcopy(puzzle)
        self.puzzle[x][y], self.puzzle[newX][newY] = self.puzzle[newX][newY], self.puzzle[x][y]
        self.x = newX
        self.y = newY
        self.depth = depth
        self.parent = parent

# Function to check if two states are equal
def is_goal(puzzle):
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] != goal[i][j]:
                return False
    return True

# Function to print the puzzle
def print_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(map(str, row)))
    print()

# Function to print the steps leading to the solution
def print_solution(node):
    if node is None:
        return
    print_solution(node.parent)
    print_puzzle(node.puzzle)

# BFS implementation
def bfs(start, x, y):
    queue = deque()
    root = Node(start, x, y, x, y, 0, None)
    queue.append(root)

    while queue:
        current = queue.popleft()

        if is_goal(current.puzzle):
            print(f"Solution found at depth: {current.depth}")
            print_solution(current)
            return

        for i in range(4):
            newX = current.x + dx[i]
            newY = current.y + dy[i]

            if 0 <= newX < N and 0 <= newY < N:
                child = Node(current.puzzle, current.x, current.y, newX, newY, current.depth + 1, current)
                queue.append(child)

def main():
    start = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]

    x = y = 0
    for i in range(N):
        for j in range(N):
            if start[i][j] == 0:
                x, y = i, j

    bfs(start, x, y)

if __name__ == "__main__":
    main()
