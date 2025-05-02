import heapq

MAX_CITIES = 100
INF = float('inf')

# Graph adjacency list (each city maps to a list of tuples (neighbor, cost))
graph = [[] for _ in range(MAX_CITIES)]
numCities = 0

# Function to add an edge
def add_edge(city1, city2, cost):
    graph[city1].append((city2, cost))
    graph[city2].append((city1, cost))

# Best First Search using priority queue
def best_first_search(start, goal):
    visited = [False] * MAX_CITIES
    parent = [-1] * MAX_CITIES
    total_cost = 0

    # Priority queue elements: (cost, city)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, city = heapq.heappop(pq)

        if visited[city]:
            continue

        visited[city] = True
        total_cost += cost

        print(f"Visiting City {city} (Cost: {cost})")

        if city == goal:
            print(f"Reached destination City {goal}! Total cost: {total_cost}")
            # Reconstruct and print path
            path = []
            while city != -1:
                path.append(city)
                city = parent[city]
            print("Path:", ' '.join(map(str, reversed(path))))
            return

        for neighbor, edge_cost in graph[city]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_cost, neighbor))
                parent[neighbor] = city

    print(f"No path found from City {start} to City {goal}.")

# Main function logic
def main():
    global numCities
    numCities = 6

    # Add roads (edges)
    add_edge(0, 1, 4)
    add_edge(0, 2, 2)
    add_edge(1, 2, 5)
    add_edge(1, 3, 10)
    add_edge(2, 3, 3)
    add_edge(3, 4, 8)
    add_edge(4, 5, 6)

    start = 0
    goal = 5
    print(f"Shortest Path from City {start} to City {goal}")
    best_first_search(start, goal)

if __name__ == "__main__":
    main()
