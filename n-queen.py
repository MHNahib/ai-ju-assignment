def solve_n_queens(n):
    queens = [-1] * n
    result = []
    place_queens(queens, 0, n, result)
    return result

def place_queens(queens, row, n, result):
    if row == n:
        result.append(queens[:])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            place_queens(queens, row + 1, n, result)

def is_safe(queens, row, col):
    for i in range(row):
        if queens[i] == col or queens[i] - i == col - row or queens[i] + i == col + row:
            return False
    return True

def print_board(queens):
    for row in range(len(queens)):
        line = ""
        for col in range(len(queens)):
            if queens[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    n = int(input("Enter the board size: "))
    solutions = solve_n_queens(n)

    for solution in solutions:
        print_board(solution)
