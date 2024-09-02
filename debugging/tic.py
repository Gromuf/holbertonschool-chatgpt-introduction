#!/usr/bin/python3

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if (
            board[0][col] == board[1][col] == board[2][col] and
            board[0][col] != " "
        ):
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and any(" " in row for row in board):
        print_board(board)
        while True:
            try:
                row = int(input(
                    f"Enter row (0, 1, or 2) for player {player}: "
                    ))
                col = int(input(
                    f"Enter column (0, 1, or 2) for player {player}: "
                    ))
                if row in range(3) and col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        player = "O" if player == "X" else "X"

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    tic_tac_toe()
