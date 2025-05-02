import random

# Function to create a blank crossword grid with walls around
def create_grid(N):
    grid = [['-' for _ in range(N)] for _ in range(N)]
    
    # Add a border of walls (#)
    for i in range(N):
        grid[0][i] = grid[N-1][i] = '#'
        grid[i][0] = grid[i][N-1] = '#'
    
    return grid

# Function to check if a word can be placed horizontally
def canPlaceHorizontally(row, col, word):
    length = len(word)
    if col + length > N:
        return False  # Out of bounds

    for i in range(length):
        if grid[row][col + i] != '-' and grid[row][col + i] != word[i]:
            return False
    return True

# Function to check if a word can be placed vertically
def canPlaceVertically(row, col, word):
    length = len(word)
    if row + length > N:
        return False  # Out of bounds

    for i in range(length):
        if grid[row + i][col] != '-' and grid[row + i][col] != word[i]:
            return False
    return True

# Place the word horizontally and store the original characters for backtracking
def placeWordHorizontally(row, col, word, backup):
    length = len(word)
    for i in range(length):
        backup[i] = grid[row][col + i]  # Save backup
        grid[row][col + i] = word[i]    # Place word

# Place the word vertically and store the original characters for backtracking
def placeWordVertically(row, col, word, backup):
    length = len(word)
    for i in range(length):
        backup[i] = grid[row + i][col]  # Save backup
        grid[row + i][col] = word[i]    # Place word

# Restore horizontal word placement (backtracking)
def restoreWordHorizontally(row, col, word, backup):
    length = len(word)
    for i in range(length):
        grid[row][col + i] = backup[i]  # Restore original

# Restore vertical word placement (backtracking)
def restoreWordVertically(row, col, word, backup):
    length = len(word)
    for i in range(length):
        grid[row + i][col] = backup[i]  # Restore original

# Recursive function to place words in the crossword
def solve(index):
    if index == WORDS:
        return True  # All words placed

    backup = [''] * N  # Backup for backtracking

    for row in range(N):
        for col in range(N):
            # Try placing the word horizontally
            if canPlaceHorizontally(row, col, words[index]):
                placeWordHorizontally(row, col, words[index], backup)
                if solve(index + 1):
                    return True
                restoreWordHorizontally(row, col, words[index], backup)

            # Try placing the word vertically
            if canPlaceVertically(row, col, words[index]):
                placeWordVertically(row, col, words[index], backup)
                if solve(index + 1):
                    return True
                restoreWordVertically(row, col, words[index], backup)
    return False  # No valid placement found

# Function to print the crossword grid
def printGrid():
    for row in range(N):
        print(' '.join(grid[row]))

# Main function
if __name__ == "__main__":
    N = int(input("Enter the grid size (N): "))  # Grid size

    # Input the words to place
    WORDS = int(input("Enter the number of words: "))
    words = []
    print(f"Enter {WORDS} words to place:")
    for _ in range(WORDS):
        words.append(input("Enter a word: "))

    # Create the grid with walls and empty spaces
    grid = create_grid(N)

    # Solve the crossword puzzle
    if solve(0):
        print("Crossword Solution Found:")
        printGrid()
    else:
        print("No solution found. Try increasing grid size or modifying word list.")
