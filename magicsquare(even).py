def generate_magic_square(n):
    if n < 3:
        raise ValueError("Magic square not possible for n < 3.")

    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        next_i, next_j = (i - 1) % n, (j + 1) % n
        if magic_square[next_i][next_j]:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = [[(n * i) + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                magic_square[i][j] = (n * n + 1) - magic_square[i][j]
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square_size = half_n
    sub_square = generate_odd_magic_square(half_n)
    magic_square = [[0] * n for _ in range(n)]

    # Constants for quadrants
    add = [0, 2, 3, 1]
    for i in range(half_n):
        for j in range(half_n):
            for k in range(4):
                row = i + (k // 2) * half_n
                col = j + (k % 2) * half_n
                magic_square[row][col] = sub_square[i][j] + add[k] * half_n * half_n

    # Swap specific columns between top-left and bottom-left
    num_swaps = half_n // 2
    for i in range(n):
        for j in range(num_swaps):
            if j == num_swaps and i >= half_n:
                continue
            if i < half_n:
                magic_square[i][j], magic_square[i + half_n][j] = magic_square[i + half_n][j], magic_square[i][j]

    # Special center column swap
    col = num_swaps
    for i in range(half_n):
        magic_square[i][col], magic_square[i + half_n][col] = magic_square[i + half_n][col], magic_square[i][col]

    return magic_square

def print_magic_square(square):
    print("Magic Square:")
    for row in square:
        print(" ".join(f"{num:3}" for num in row))
    print(f"Magic Sum: {sum(square[0])}")

# Main Program
try:
    n = int(input("Enter the size of the magic square (>=3): "))
    magic_square = generate_magic_square(n)
    print_magic_square(magic_square)
except ValueError as e:
    print(e)
