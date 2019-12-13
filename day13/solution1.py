from collections import defaultdict
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

screen = defaultdict(int)
solver = Solver(int_code_program, [])
while not solver.is_finished:
    x = solver.solve()
    y = solver.solve()
    tile_id = solver.solve()
    screen[x, y] = tile_id

print(sum(1 for tile_id in screen.values() if tile_id == 2))
