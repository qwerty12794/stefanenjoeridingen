import time

# helper function
def cross(A, B):
    # cross product of chars in string A and chars in string B
    return [a+b for a in A for b in B]

#   1 2 3 4 .. 9
# A
# B
# C
# D
# ..
# I

digits = '123456789'
rows   = 'ABCDEFGHI'
cols   = digits
cells  = cross(rows, cols) # for 3x3 81 cells A1..9, B1..9, C1..9, ... 

# unit = a row, a column, a box; list of all units
unit_list = ([cross(r, cols) for r in rows] +                             # 9 rows 
             [cross(rows, c) for c in cols] +                             # 9 cols
             [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]) # 9 units
# peers is a dict {cell : list of peers}
# every cell c has 20 peers p (i.e. cells that share a row, col, box)
# units['A1'] is a list of lists, and sum(units['A1'],[]) flattens this list
units = dict((s, [u for u in unit_list if s in u]) for s in cells)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in cells)

def test():
    # a set of tests that must pass
    assert len(cells) == 81
    assert len(unit_list) == 27
    assert all(len(units[s]) == 3 for s in cells)
    assert all(len(peers[s]) == 20 for s in cells)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print ('All tests pass.')

def display(grid):
    # grid is a dict of {cell: string}, e.g. grid['A1'] = '1234'
    print()
    for r in rows:
        for c in cols:
            v = grid[r+c]
            # avoid the '123456789'
            if v == '123456789': 
                v = '.'
            print (''.join(v), end=' ')
            if c == '3' or c == '6': print('|', end='')
        print()
        if r == 'C' or r == 'F': 
            print('-------------------')
    print()

def parse_string_to_dict(grid_string):
    # grid_string is a string like '4.....8.5.3..........7......2.....6....   '
    # convert grid_string into a dict of {cell: chars}
    char_list1 = [c for c in grid_string if c in digits or c == '.']
    # char_list1 = ['8', '5', '.', '.', '.', '2', '4', ...  ]
    assert len(char_list1) == 81

    print(char_list1)

    # replace '.' with '1234567'
    char_list2 = [s.replace('.', '123456789') for s in char_list1]

    # grid {'A1': '8', 'A2': '5', 'A3': '123456789',  }
    return dict(zip(cells, char_list2))

def no_conflict(grid, c, v):
    # check if assignment is possible: value v not a value of a peer
    for p in peers[c]:
        if grid[p] == v:
           return False # conflict
    return True


def is_valid_supuku(grid):
    for cell in cells:
        if len(grid[cell]) > 1:
            return False

    return True


def solve(grid):
    # print(grid['A9'])
    # backtracking search a solution (DFS)
    # your code here

    if is_valid_supuku(grid):
        display(grid)
        return grid

    for c in cells:
        if len(grid[c]) > 1:
            # print(grid[c])
            possible_values = grid[c]
            possible_number_list = list(possible_values)
            # print(possible_number_list)

            for number in possible_number_list:



                if no_conflict(grid, c, number):
                    grid[c] = number
                    # print(grid[c])
                    # display(grid)

                    if solve(grid):
                        return True

                    grid[c] = possible_values
            return

            # print(c)
            # print(grid[c])


    return False

# minimum nr of clues for a unique solution is 17
s1 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
s2 = '85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.'
s3 = '...5....2...3..85997...83..53...9...19.73...4...84...1.471..6...5...41...1...6247'
s4 = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
s5 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
s6 = '8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..'
s7 = '6..3.2....5.....1..........7.26............543.........8.15........4.2........7..'
s8 = '.6.5.1.9.1...9..539....7....4.8...7.......5.8.817.5.3.....5.2............76..8...'
s9 = '..5...987.4..5...1..7......2...48....9.1.....6..2.....3..6..2.......9.7.......5..'
s10 = '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
s11 = '1.....3.8.7.4..............2.3.1...........958.........5.6...7.....8.2...4.......'
s12 = '6..3.2....4.....1..........7.26............543.........8.15........4.2........7..'
s13 = '....3..9....2....1.5.9..............1.2.8.4.6.8.5...2..75......4.1..6..3.....4.6.'
s14 = '45.....3....8.1....9...........5..9.2..7.....8.........1..4..........7.2...6..8..'
s15 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
slist = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]

for s in slist:
    d = parse_string_to_dict(s)
    display(d)
    start_time = time.time()
    solve(d)
    print(time.time()-start_time)

# d = parse_string_to_dict(s8)
# display(d)
# start_time = time.time()
# solve(d)
# print(time.time()- start_time)