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


def print_area(area, path = None):
    min_y = min(y for x, y in area)
    max_y = max(y for x, y in area)
    min_x = min(x for x, y in area)
    max_x = max(x for x, y in area)
    if path:
        x, y = 0, 0
        area[x, y] = 5
        for d in path[:-1]:
            x_diff, y_diff = DIRECTIONS_MAP[d]
            x += x_diff
            y += y_diff
            area[x, y] = 5
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if area[x, y] == 1:
                print(" ", end="")
            elif area[x, y] == 0:
                print("█", end="")
            elif area[x, y] == -1:
                print("?", end="")
            elif area[x, y] == 5:
                print(".", end="")
            elif area[x, y] == 2:
                print("$", end="")
        print()


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

todo = [((0, 0), [])]
heapify(todo)
discovered = defaultdict(lambda: -1)
discovered[0, 0] = 1
while 2 not in discovered.values():
    (x, y), path = heappop(todo)
    for direction, (x_diff, y_diff) in DIRECTIONS_MAP.items():
        new_x = x + x_diff
        new_y = y + y_diff
        if (new_x, new_y) in discovered:
            continue
        solver = Solver(int_code_program.copy(), [])
        for d in path:
            solver.input_values = iter([d])
            result = solver.solve()
        solver.input_values = iter([direction])
        result = solver.solve()
        discovered[new_x, new_y] = result
        if result == 2:
            oxygen_location = new_x, new_y
            oxygen_path = path + [direction]
            break
        if result > 0:
            heappush(todo, ((new_x, new_y), path + [direction]))

print_area(discovered, oxygen_path)
print(len(oxygen_path))
