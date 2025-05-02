def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def is_safe(board, row, col, N):
    # Check row on the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_nq_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            if solve_nq_util(board, col + 1, N):
                return True

            board[i][col] = 0  # backtrack

    return False


def solve_nq(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_solution(board, N)
    return True


if __name__ == "__main__":
    try:
        N = int(input("Enter the value of N: "))
        if N < 1:
            print("Invalid input. N must be at least 1.")
        else:
            solve_nq(N)
    except ValueError:
        print("Invalid input. Please enter an integer.")
