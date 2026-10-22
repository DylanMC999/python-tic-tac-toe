
# Tic-Tac-Toe Game
# 0 = Empty Space
# 1 = Player 1 (X)
# 2 = Player 2 (O)


def Game_Setup(game):
    # Loop through each row of the game board
    for i in range(len(game)):
        # Loop through each column in the current row
        for j in range(len(game[i])):
            # Print "-" if the position is empty
            if game[i][j] == 0:
                print("-", end=" ")
            # Print "X" if Player 1 occupies the position
            elif game[i][j] == 1:
                print("X", end=" ")
            # Print "O" if Player 2 occupies the position
            elif game[i][j] == 2:
                print("O", end=" ")
            # Print an error if the value is invalid
            else:
                print("Error", end=" ")
        # Move to the next row after printing each column
        print()


def Set_Loc(game, row, col, team):
    # Place the current player's mark at the selected position
    game[row][col] = team


def Check_Win(game):
    # Check all three horizontal rows for a winner
    for i in range(3):
        # If all three positions match and aren't empty, return the winner
        if game[i][0] == game[i][1] == game[i][2] != 0:
            return game[i][0]

    # Check all three vertical columns for a winner
    for j in range(3):
        # If all three positions match and aren't empty, return the winner
        if game[0][j] == game[1][j] == game[2][j] != 0:
            return game[0][j]

    # Check diagonal from top-left to bottom-right
    if game[0][0] == game[1][1] == game[2][2] != 0:
        return game[0][0]

    # Check diagonal from top-right to bottom-left
    if game[0][2] == game[1][1] == game[2][0] != 0:
        return game[0][2]

    # Return 0 if nobody has won
    return 0


def Check_Draw(game):
    # Check if a player has already won
    if Check_Win(game) != 0:
        return False

    # Loop through every position on the board
    for i in range(3):
        for j in range(3):
            # If an empty position exists, the game isn't a draw
            if game[i][j] == 0:
                return False

    # Return True if the board is full and nobody has won
    return True


def Player_Turn(game, team):
    # Keep asking until the player enters a valid move
    while True:
        # Display whose turn it is
        print("Player", team, "turn")

        try:
            # Ask the player for a row and column
            position = input("Enter position (row-col): ")

            # Split the input at "-" into row and column
            row, col = position.split("-")

            # Convert row and column from strings into integers
            row = int(row)
            col = int(col)

            # Check if the selected position is outside the board
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position! Try again.")
                continue

            # Check if another player already occupies the position
            if game[row][col] != 0:
                print("Position already taken! Try again.")
                continue

            # Place the current player's mark on the board
            Set_Loc(game, row, col, team)

            # Exit the loop after a successful move
            break

        # Handle incorrect inputs such as letters or wrong formatting
        except ValueError:
            print("Invalid input! Use row-col (example: 0-1)")


def main():
    # Create an empty 3x3 Tic-Tac-Toe board
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    # Start the game with Player 1 (X)
    team = 1

    # Display the empty board before the first turn
    Game_Setup(game)

    # Continue playing until someone wins or the game is a draw
    while True:
        # Allow the current player to choose a position
        Player_Turn(game, team)

        # Display the updated board after each move
        print()
        Game_Setup(game)
        print()

        # Check if either player has won
        winner = Check_Win(game)

        # If there is a winner, announce it and end the game
        if winner != 0:
            print("Player", winner, "Wins!")
            break

        # Check if the board is full without a winner
        if Check_Draw(game):
            print("It's a Draw!")
            break

        # Switch to the other player after a valid turn
        if team == 1:
            team = 2
        else:
            team = 1


# Run the game only when this file is executed directly
if __name__ == '__main__':
    main()
