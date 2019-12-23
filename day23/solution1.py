import itertools
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

solvers = [Solver(int_code_program.copy(), [i]) for i in range(50)]
for solver in solvers:
    solver.solve()

for i in itertools.cycle(range(50)):
    if not solvers[i].input_values:
        solvers[i].input_values = [-1]
    if destination := solvers[i].solve():
        x = solvers[i].solve()
        y = solvers[i].solve()
        if destination == 255:
            print(y)
            break
        solvers[destination].input_values.extend([x, y])
