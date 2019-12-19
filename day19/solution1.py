from collections import defaultdict
from int_code_solver import Solver

with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

grid = defaultdict(int)
for y in range(50):
    for x in range(50):
        solver = Solver(int_code_program, input_values=[x, y])
        grid[x, y] = solver.solve()
print(sum(grid.values()))

max_y = max(y for x, y in grid)
max_x = max(x for x, y in grid)
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if grid[x, y]:
            print("#", end="")
        else:
            print(" ", end="")
    print()
