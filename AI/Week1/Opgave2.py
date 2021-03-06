import random
import string


def make_board(size):
    board = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]
    return board


def get_dictionary():
    prefix = set()
    words = []

    with open('words.txt', 'r') as f:
        for word in f:
            word = word.strip()
            words.append(word)

            for i in range(len(word)):
                prefix.add(word[:i + 1])

    return words, prefix


def print_board(board):
    for row in board:
        print(' '.join([str(letter) for letter in row]))


def in_board(board, x, y):
    return 0 <= y < len(board) and 0 <= x < len(board[y])


def get_letter(board, position):
    return board[position[0], position[1]]


def get_neighboars(board, row, col):
    adj = []
    length = len(board) - 1

    postitions = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
    for pos in postitions:
        row = pos[0]
        col = pos[1]
        if row < 0:
            row = length
        elif row > length:
            row = 0
        if col < 0:
            col = length
        elif col > length:
            col = 0
        adj.append((row, col))
    return adj


words, prefixes = get_dictionary()


def dfs(board, found, row, col, path=None, word=None):
    letter = board[row][col]

    if path is None or word is None:
        path = [(row, col)]
        word = letter
    else:
        path.append((row, col))
        word = word + letter

        if word not in prefixes:
            return

    print(path)
    print(word)

    if word in words:

        found.add(word)

    for neighbor in get_neighboars(board, row, col):
        if neighbor not in path:
            dfs(board, found, neighbor[0], neighbor[1], path[:], word[:])
        else:
            print("niets gevonden in ", path)


def play_boggle(board, found):
    for r in range(len(board)):
        for c in range(len(board)):
            dfs(board, found, r, c)


board = make_board(4)
print_board(board)

found = set()
play_boggle(board, found)

print(found)

print_board(board)
