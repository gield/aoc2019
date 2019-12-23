import itertools
from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

solvers = [Solver(int_code_program.copy(), [i]) for i in range(50)]
for solver in solvers:
    solver.solve()

previous_nat = None
nat = None
network_is_idle = True
for i in itertools.cycle(range(50)):
    if not solvers[i].input_values:
        solvers[i].input_values = [-1]
    else:
        network_is_idle = False
    if destination := solvers[i].solve():
        x = solvers[i].solve()
        y = solvers[i].solve()
        if destination == 255:
            nat = (x, y)
        else:
            solvers[destination].input_values.extend([x, y])

    if i == 0:
        if network_is_idle and nat:
            if previous_nat and nat[1] == previous_nat[1]:
                print(nat[1])
                break
            solvers[i].input_values.extend(list(nat))
            previous_nat, nat = nat, None
        network_is_idle = True
