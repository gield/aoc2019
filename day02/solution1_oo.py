from typing import Any, List, Tuple


class Solver:

    def __init__(self, memory: List[int]) -> None:
        self.memory = memory
        self.pointer = 0
        self.is_finished = False

        self.OPERATIONS = {
            1: self.add,
            2: self.multiply,
            99: self.finish,
        }
        self.NUMBER_OF_PARAMETERS = {
            1: 3,
            2: 3,
            99: 0,
        }

    def solve(self) -> List[int]:
        while not self.is_finished:
            self.step()
        return self.memory

    def step(self) -> None:
        operation, params = self.read_instruction()
        operation(*params)

    def read_instruction(self) -> Tuple[Any, List[int]]:
        opcode = self.memory[self.pointer]
        operation = self.OPERATIONS[opcode]
        n_params = self.NUMBER_OF_PARAMETERS[opcode]
        if n_params > 0:
            start = self.pointer + 1
            end = self.pointer + n_params + 1
            params = self.memory[start:end]
        else:
            params = []
        self.pointer += n_params + 1
        return operation, params

    # OPERATIONS
    def add(self, p1: int, p2: int, p3: int) -> None:
        self.memory[p3] = self.memory[p1] + self.memory[p2]

    def multiply(self, p1: int, p2: int, p3: int) -> None:
        self.memory[p3] = self.memory[p1] * self.memory[p2]

    def finish(self) -> None:
        self.is_finished = True


with open("input.txt") as input_file:
    memory = list(map(int, input_file.readline().split(",")))
memory[1] = 12
memory[2] = 2

solver = Solver(memory)
output = solver.solve()
print(output[0])
