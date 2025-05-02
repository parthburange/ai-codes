# Map Coloring Problem using Backtracking

# List of adjacent regions (graph structure)
# Regions are numbered 0 to 4 (you can extend it for more regions)
adjacency_list = {
    0: [1, 2],  # Region 0 is adjacent to Region 1 and 2
    1: [0, 3, 4],  # Region 1 is adjacent to Region 0, 3, and 4
    2: [0, 4],  # Region 2 is adjacent to Region 0 and 4
    3: [1],  # Region 3 is adjacent to Region 1
    4: [1, 2]  # Region 4 is adjacent to Region 1 and 2
}

# Colors available (3 colors: Red, Green, Blue)
colors = ['Red', 'Green', 'Blue']

# Function to check if current assignment is valid
def is_valid_assignment(region, color, assignment):
    for neighbor in adjacency_list[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False  # Neighbor has the same color
    return True

# Backtracking function to assign colors to regions
def map_coloring(assignment):
    # If assignment is complete, return True
    if len(assignment) == len(adjacency_list):
        return True

    # Select an uncolored region (choose a region not in the assignment yet)
    region = len(assignment)  # Regions are numbered from 0 to n-1
    
    # Try each color from the domain
    for color in colors:
        if is_valid_assignment(region, color, assignment):
            assignment[region] = color  # Assign color to the region

            # Recurse to assign colors to the rest of the regions
            if map_coloring(assignment):
                return True

            # If no solution, backtrack and remove the color assignment
            del assignment[region]
    
    # If no valid assignment found, return False
    return False

# Function to solve the map coloring problem
def solve_map_coloring():
    assignment = {}
    if map_coloring(assignment):
        return assignment
    else:
        return "No solution found"

# Solve the problem
solution = solve_map_coloring()
print("Solution:", solution)
