import random
import time

# Define the game board
board = [[' ' for x in range(10)] for y in range(20)]

# Define the shapes of the blocks
shapes = [
    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],

    [['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']]
]

# Define the colors of the blocks
colors = ['R', 'G', 'B', 'Y', 'O', 'P', 'C']

# Define the current block
current_block = random.choice(shapes)
current_color = random.choice(colors)

# Define the current position of the block
current_x = 4
current_y = 0

# Define the score
score = 0

# Define the game loop
while True:
    # Clear the screen
    print('\033[H\033[J')

    # Print the game board
    for row in board:
        print(' '.join(row))

    # Print the score
    print('Score:', score)

    # Move the block down
    current_y += 1

    # Check if the block has collided with the bottom or another block
    if current_y + len(current_block) > len(board):
        current_y -= 1
        for i in range(len(current_block)):
            for j in range(len(current_block[i])):
                if current_block[i][j] != '.':
                    board[current_y + i][current_x + j] = current_color
                    current_block = random.choice(shapes)
                    current_color = random.choice(colors)
                    current_x =4

    # Check if any rows are complete and remove them
    complete_rows = []
    for i in range(len(board)):
        if '.' not in board[i]:
            complete_rows.append(i)
    for row in complete_rows:
        del board[row]
        board.insert(0, [' ' for x in range(10)])
        score += 10

    # Check if the game is over
    if any(board[0]):
        print('Game Over')
        print('Final Score:', score)
        break

    # Wait for a moment before continuing
    time.sleep(0.5)
    # Wait for user input to continue
    input('Press Enter to continue...')
