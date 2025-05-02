MAX = 10  # Digits 0-9

# Characters in the problem: S, E, N, D, M, O, R, Y
letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
assigned = [-1] * 26  # Maps letters to digits
used = [False] * MAX  # Tracks used digits

# Function to get the numerical value of the word
def get_value(word):
    value = 0
    for char in word:
        value = value * 10 + assigned[ord(char) - ord('A')]
    return value

# Check if the current assignment is valid
def is_valid():
    send = get_value("SEND")
    more = get_value("MORE")
    money = get_value("MONEY")
    return (send + more == money)

# Backtracking function to solve the problem
def solve(index):
    if index == 8:  # All letters are assigned
        return is_valid()

    for digit in range(MAX):
        if not used[digit]:
            assigned[ord(letters[index]) - ord('A')] = digit
            used[digit] = True

            if solve(index + 1):
                return True

            # Backtrack
            used[digit] = False

    return False

# Main function to execute the program
def main():
    if solve(0):
        print("Solution:")
        send = get_value("SEND")
        more = get_value("MORE")
        money = get_value("MONEY")
        
        # Print the letter-to-digit assignments
        for i in range(8):
            print(f"{letters[i]} = {assigned[ord(letters[i]) - ord('A')]}")
        
        # Print the sum and result
        print(f"\n{send} + {more} = {money}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
