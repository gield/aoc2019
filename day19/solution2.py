from collections import defaultdict
from itertools import count
from typing import Tuple

from int_code_solver import Solver


def is_beam(x: int, y: int) -> bool:
    if (x, y) not in grid:
        solver = Solver(int_code_program, input_values=[x, y])
        grid[x, y] = solver.solve()
    return grid[x, y] == 1


def get_square(size: int) -> Tuple[int, int]:
    x_first = 0  # Don't naively start counting from 0 on each row
    for y in count():
        if y in {1, 2, 3}:  # Speed-up: these lines don't contain the beam
            continue
        currently_in_beam = False
        for x in count(x_first):
            if not is_beam(x, y):  # We are currently not in the beam
                if currently_in_beam:
                    break  # We have passed the beam
                else:
                    continue # We are not yet in the beam
            if not currently_in_beam:
                currently_in_beam = True
                x_first = x  # Next row, start checking a bit further
            if is_beam(x + size - 1, y) and is_beam(x, y + size - 1) and \
                    is_beam(x + size - 1, y + size - 1):
                return x, y


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

grid = defaultdict(int)  # Oops global variable
x_square, y_square = get_square(100)
print(x_square * 10_000 + y_square)
