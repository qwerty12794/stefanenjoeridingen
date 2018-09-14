import random
import string


class Board():

    filled_board = []

    def __init__(self, size):
        self.filled_board = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]

    def get_board(self):
        return self.filled_board

class Testboard():

    filled_board = []

    def __init__(self):
        line_one = ['a', 'c', 'h', 't', 'x', 'x', 'o']
        line_two = ['o', 'g', 'e', 'n', 'x', 'x', 'l']
        line_three = ['c', 'e', 's', 'k', 'p', 'a', 'i']
        line_four = ['x', 'x', 'x', 'o', 'x', 'x', 'e']
        line_five = ['x', 'x', 'h', 'x', 'x', 'x', 'x']
        line_six = ['x', 'c', 'x', 'o', 'x', 'x', 'x']
        line_seven = ['s', 'x', 'x', 'x', 'm', 'x', 'x']

        self.filled_board = [line_one, line_two, line_three, line_four, line_five, line_six, line_seven]

    def get_board(self):
        return self.filled_board


class Utils():
    @staticmethod
    def words_from_file_to_set():
        set_of_words = set()
        with open('words.txt') as f:
            for line in f:
                set_of_words.add(line.strip("\n"))
        return set_of_words


board = Testboard().get_board()

# for line in board:
#     print(line)

#---https://stackoverflow.com/questions/1620940/determining-neighbours-of-cell-two-dimensional-list---

X=7
Y=7

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                           for y2 in range(y-1, y+2)
                           if (-1 < x <= X and
                               -1 < y <= Y and
                               (x != x2 or y != y2) and
                               (0 <= x2 <= X) and
                               (0 <= y2 <= Y))]

print(neighbors(2,2))

for i in list:
    print(i)



# print(list(Utils.words_to_set()))


    # with open('words.txt', 'rt', encoding='utf-8') as f:
    #     print(f.read())