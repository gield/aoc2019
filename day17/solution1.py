from collections import defaultdict
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

screen = defaultdict(lambda: "?")
solver = Solver(int_code_program)
x, y = 0, 0
while output := solver.solve():
    if chr(output) == "\n":
        y += 1
        x = 0
    else:
        screen[x, y] = chr(output)
        x += 1

min_y = min(y for x, y in screen)
max_y = max(y for x, y in screen)
min_x = min(x for x, y in screen)
max_x = max(x for x, y in screen)
total_sum = 0
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if screen[x, y] == "#" \
                and x - 1 >= min_x and x + 1 <= max_x \
                and y - 1 >= min_y and y + 1 <= max_y \
                and screen[x - 1, y] == "#" and screen[x + 1, y] == "#" \
                and screen[x, y - 1] == "#" and screen[x, y + 1] == "#":
            total_sum += x * y
print(total_sum)
