from heapq import heapify, heappop, heappush
import random
from collections import defaultdict
from int_code_solver import Solver


NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
DIRECTIONS_MAP = {
    NORTH: (0, -1),
    SOUTH: (0, 1),
    WEST: (-1, 0,),
    EAST: (1, 0),
}

with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

todo = [((0, 0), [])]
heapify(todo)
discovered = defaultdict(lambda: -1)
discovered[0, 0] = 1
while todo:
    (x, y), path = heappop(todo)
    for direction, (x_diff, y_diff) in DIRECTIONS_MAP.items():
        new_x = x + x_diff
        new_y = y + y_diff
        if (new_x, new_y) in discovered:
            continue
        solver = Solver(int_code_program.copy())
        for d in path:
            result = solver.solve(d)
        result = solver.solve(direction)
        discovered[new_x, new_y] = result
        if result == 2:
            oxygen_location = new_x, new_y
            oxygen_path = path + [direction]
        if result > 0:
            heappush(todo, ((new_x, new_y), path + [direction]))

todo = [(0, oxygen_location)]
heapify(todo)
visited = set()
highest_cost = 0
while todo:
    cost, (x, y) = heappop(todo)
    if cost > highest_cost:
        highest_cost = cost
    for direction, (x_diff, y_diff) in DIRECTIONS_MAP.items():
        new_x = x + x_diff
        new_y = y + y_diff
        if (new_x, new_y) not in visited and discovered[new_x, new_y] != 0:
            visited.add((new_x, new_y))
            heappush(todo, (cost + 1, (new_x, new_y)))
print(highest_cost)
