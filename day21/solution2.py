from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))

# try to land on the fourth tile in front of the robot
# plus also check if you can jump after that fourth tile
# = D and (not A or not B or not C)
#   and (E or H)
solution = list("""
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
""")
int_solution = [ord(c) for c in solution[1:]]
solver = Solver(int_code_program, input_values=int_solution)
while not solver.is_finished:
    output = solver.solve()
    if output and output <= 126:
        print(chr(output), end="")
    elif output:
        print(output)
