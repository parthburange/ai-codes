import heapq

ROW = 5
COL = 5

# Node class to hold coordinates and heuristic cost
class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost  # Needed for priority queue

# Manhattan Distance heuristic
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Directions: up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Best First Search implementation
def best_first_search(grid, startX, startY, goalX, goalY):
    visited = [[0 for _ in range(COL)] for _ in range(ROW)]
    pq = []
    start_node = Node(startX, startY, heuristic(startX, startY, goalX, goalY))
    heapq.heappush(pq, start_node)

    print("Path:")
    while pq:
        current = heapq.heappop(pq)

        if visited[current.x][current.y]:
            continue

        visited[current.x][current.y] = 1

        if current.x == goalX and current.y == goalY:
            print(f"({current.x}, {current.y})")
            print("Reached Goal!")
            return

        print(f"({current.x}, {current.y}) -> ", end='')

        for i in range(4):
            nx = current.x + dx[i]
            ny = current.y + dy[i]

            if 0 <= nx < ROW and 0 <= ny < COL and grid[nx][ny] == 0 and not visited[nx][ny]:
                neighbor = Node(nx, ny, heuristic(nx, ny, goalX, goalY))
                heapq.heappush(pq, neighbor)

    print("\nGoal not reachable!")

def main():
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    startX, startY = 0, 0
    goalX, goalY = 4, 4
    best_first_search(grid, startX, startY, goalX, goalY)

if __name__ == "__main__":
    main()
