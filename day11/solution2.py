from collections import defaultdict
from int_code_solver import Solver
from typing import List, Tuple


class Robot:

    def __init__(self, int_code_program: List[int], hull) -> None:
        self.dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.hull = hull
        self.x, self.y = 0, 0
        self.direction = 0
        self.solver = Solver(int_code_program)
        self.seen = set()

    def paint(self) -> None:
        while not self.solver.is_finished:
            color = self.solver.solve(self.hull[self.x, self.y])
            turn = self.solver.solve()
            self.hull[self.x, self.y] = color
            self.seen.add((self.x, self.y))
            self.move(-1 if turn == 0 else 1)

    def move(self, turn: int) -> None:
        self.direction = (self.direction + turn) % 4
        self.x += self.dirs[self.direction][0]
        self.y += self.dirs[self.direction][1]


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

hull = defaultdict(int)
hull[0, 0] = 1
r = Robot(int_code_program, hull)
r.paint()

max_y = max(y for x, y in r.hull)
max_x = max(x for x, y in r.hull)
for y in range(max_y + 1):
    for x in range(max_x + 1):
        print("█" if r.hull[x, y] else " ", end="")
    print()
