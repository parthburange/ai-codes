import heapq

def dijkstra(graph, start, goal):
    # Initialize the distance dictionary and priority queue
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, city)
    previous_cities = {city: None for city in graph}
    
    # Display initial state
    print(f"Initial state: {distances}\n")

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # Early exit if we reached the goal
        if current_city == goal:
            break

        # Check neighbors and update distances
        for neighbor, distance in graph[current_city].items():
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_cities[neighbor] = current_city
                heapq.heappush(priority_queue, (new_distance, neighbor))

        # Display the current step and distances
        print(f"Move to {current_city} with distance: {current_distance}")
        print("Current distance matrix:")
        for city, dist in distances.items():
            print(f"{city}: {dist}")
        print("---")

    # Reconstruct the shortest path
    path = []
    current_city = goal
    while current_city is not None:
        path.append(current_city)
        current_city = previous_cities[current_city]
    
    return distances[goal], path[::-1]  # Return distance and path in correct order

# ---------------- STATIC ----------------

def main():
    # Hardcoded graph: city -> {neighbor_city: distance}
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3},
        'D': {'B': 10, 'C': 3}
    }

    # Hardcoded start and goal cities
    start = 'A'
    goal = 'D'

    distance, path = dijkstra(graph, start, goal)

    if distance != float('inf'):
        print(f"\nThe shortest path from {start} to {goal} is {distance} with the path:")
        print(" -> ".join(path))
    else:
        print(f"No path found from {start} to {goal}.")

if __name__ == "__main__":
    main()

