from collections import defaultdict
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))
int_code_program[0] = 2

screen = defaultdict(int)
solver = Solver(int_code_program)
x_paddle, x_ball = 0, 0
next_input = None
while not solver.is_finished:
    x = solver.solve(next_input)
    y = solver.solve()
    tile_id = solver.solve()
    if x == -1 and y == 0:
        score = tile_id
    else:
        screen[x, y] = tile_id

    x_paddle = x if tile_id == 3 else x_paddle
    x_ball = x if tile_id == 4 else x_ball
    if x_ball > x_paddle:
        next_input = 1
    elif x_ball < x_paddle:
        next_input = -1
    else:
        next_input = 0

print(score)
