from int_code_solver import Solver


with open("input.txt") as f:
    int_code_program = list(map(int, f.readline().strip().split(",")))
int_code_program[0] = 2

# MAIN = A,A,B,C,A,C,B,C,A,B
# A = L,4,L10,L,6
# B = L,6,L,4,R,8,R,8
# C = L,6,R,8,L,10,L,8,L,8
solution = list("""A,A,B,C,A,C,B,C,A,B
L,4,L,10,L,6
L,6,L,4,R,8,R,8
L,6,R,8,L,10,L,8,L,8
n
""")
int_solution = [ord(c) for c in solution]
solver = Solver(int_code_program, input_values=int_solution)
while not solver.is_finished:
    output = solver.solve()
    if output and output <= 126:
        print(chr(output), end="")
    elif output:
        print(output)
