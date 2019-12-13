from collections import defaultdict
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))
int_code_program[0] = 2

screen = defaultdict(int)
solver = Solver(int_code_program, [])
x_paddle, x_ball = 0, 0
while not solver.is_finished:
    x = solver.solve()
    y = solver.solve()
    tile_id = solver.solve()
    if x == -1 and y == 0:
        score = tile_id
    else:
        screen[x, y] = tile_id

    x_paddle = x if tile_id == 3 else x_paddle
    x_ball = x if tile_id == 4 else x_ball
    if x_ball > x_paddle:
        solver.input_values = iter([1])
    elif x_ball < x_paddle:
        solver.input_values = iter([-1])
    else:
        solver.input_values = iter([0])

print(score)
