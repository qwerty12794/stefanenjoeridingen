import heapq
import math
import numpy as np


class PriorityQueue:
    # to be use in the A* algorithm
    # a wrapper around heapq (aka priority queue), a binary min-heap on top of a list
    # in a min-heap, the keys of parent nodes are less than or equal to those
    # of the children and the lowest key is in the root node
    def __init__(self):
        # create a min heap (as a list)
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    # heap elements are tuples (priority, item)
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # pop returns the smallest item from the heap
    # i.e. the root element = element (priority, item) with highest priority
    def get(self):
        return heapq.heappop(self.elements)[1]


def get_matrix(string):
    a = list(map(int, string.split()))

    length = len(a)
    nrcols = math.sqrt(length)

    matrix = np.reshape(a, (-1, int(nrcols)))
    return matrix


def get_string(matrix):
    string = ''
    for row in matrix:
        string += ' '.join(str(e) for e in row)
        string += ' '
    return string.rstrip()


def print_board(grid):
    for row in grid:
        print(row)


def get_empty_location(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                return (row, col)


def get_neighbor(node):
        neighbors = []

        grid = get_matrix(node)
        length = len(grid) - 1

        position = get_empty_location(grid)

        (row, col) = position

        positions = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
        for pos in positions:
            if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
                temp_row = pos[0]
                temp_col = pos[1]

                #   swap values
                swap_value = grid[temp_row][temp_col]
                grid[row][col] = swap_value
                grid[temp_row][temp_col] = 0
                neighbors.append(get_string(grid))
                #   revert swap values
                grid[temp_row][temp_col] = swap_value
                grid[row][col] = 0
        return neighbors


def heuristic(node):
    grid = get_matrix(node)
    manhatten_distance = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            value = grid[row][col]
            if value != 0:
                target_x = math.floor((value - 1) / len(grid))   # expected x value in matrix
                target_y = (value - 1) % len(grid)               # expected y value in matrix

                dx = row - target_x                              # optimal distance x value in matrix
                dy = col - target_y                              # optimal distance y value in matrix
                manhatten_distance += (abs(dx) + abs(dy))
    return manhatten_distance


def a_star_search(start_for_search, goal_for_search):
    queue = PriorityQueue()
    queue.put(start_for_search, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start_for_search] = None
    cost_so_far[start_for_search] = 0

    while not queue.empty():
        current = queue.get()

        if current == goal_for_search:
            string = get_matrix(current)
            print_board(string)
            print('de nr of states = ', cost_so_far[current])
            break
        for next in get_neighbor(current):

            new_cost = cost_so_far[current] + 1

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                queue.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def dijkstra(start_for_search, goal_for_search):
    frontier = PriorityQueue()
    frontier.put(start_for_search, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start_for_search] = None
    cost_so_far[start_for_search] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal_for_search:
            print_board(get_matrix(current))
            print('nr of states = ', cost_so_far[current])
            break
        for next in get_neighbor(current):
            new_cost = cost_so_far[current] + 1

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


board = "8 6 7 2 5 4 3 0 1"

goal = "1 2 3 4 5 6 7 8 0"

neighbor_string = '1 2 3 4 0 5 6 7 8'

four_board = '1 5 10 9 15 0 4 14 12 2 8 13 11 7 3 6'

four_goal = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0'


print(get_matrix(board))

came_from2_, cost_so_far = a_star_search(board, goal)
