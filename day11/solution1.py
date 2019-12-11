from collections import defaultdict
from int_code_solver import Solver
from typing import List, Tuple


class Robot:

    def __init__(self, int_code_program: List[int], hull) -> None:
        self.hull = hull
        self.x, self.y = 0, 0
        self.direction = 0
        self.solver = Solver(int_code_program, [self.hull[self.x, self.y]])
        self.seen = set()

    def paint(self) -> None:
        self.solver.solve()
        while not self.solver.is_finished:
            color = self.solver.output[-1]
            self.solver.solve()
            turn = self.solver.output[-1]
            self.hull[self.x, self.y] = color
            self.seen.add((self.x, self.y))
            self.move(-1 if turn == 0 else 1)

            self.solver.input_values = iter([self.hull[self.x, self.y]])
            self.solver.solve()

    def move(self, turn: int) -> None:
        self.direction = (self.direction + turn) % 4
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

hull = defaultdict(int)
r = Robot(int_code_program, hull)
r.paint()
print(len(r.seen))
