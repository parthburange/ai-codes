def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("This method works only for odd-order magic squares.")

    # Initialize an empty n x n grid
    magic_square = [[0] * n for _ in range(n)]

    # Start position for 1
    i, j = 0, n // 2

    # Fill the grid with numbers from 1 to n*n
    for num in range(1, n * n + 1):
        magic_square[i][j] = num

        # Calculate the next position
        next_i = (i - 1) % n
        next_j = (j + 1) % n

        # If the next cell is already filled, move down instead
        if magic_square[next_i][next_j] != 0:
            next_i = (i + 1) % n
            next_j = j
        # Update the current position
        i, j = next_i, next_j

    return magic_square

def print_magic_square(square):
    print("Magic Square:")
    for row in square:
        print(" ".join(f"{num:2}" for num in row))
    print(f"Magic Sum: {sum(square[0])}")
# Take user input
try:
    n = int(input("Enter the size of the magic square (odd number): "))
    if n % 2 == 0:
        raise ValueError("This method works only for odd-order magic squares.")
    magic_square = generate_magic_square(n)
    print_magic_square(magic_square)
except ValueError as e:
    print(e)


