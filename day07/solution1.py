import itertools
from typing import Any, List, Tuple


class Solver:

    def __init__(self, memory: List[int], input_values: List[int]) -> None:
        self.memory = memory
        self.pointer = 0
        self.is_finished = False
        self.input_values = iter(input_values)

        self.OPERATIONS = {
            1: self.add,
            2: self.multiply,
            3: self.take_input,
            4: self.print_output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            99: self.finish,
        }
        self.NUMBER_OF_PARAMETERS = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0,
        }

    def solve(self) -> int:
        while not self.is_finished:
            self.step()
        return self.output

    def step(self) -> None:
        operation, params = self.read_instruction()
        operation(*params)

    def read_instruction(self) -> Tuple[Any, List[int]]:
        instruction = self.memory[self.pointer]
        raw_param_modes, opcode = divmod(instruction, 100)
        if opcode == 0:
            print(instruction)
        operation = self.OPERATIONS[opcode]
        n_params = self.NUMBER_OF_PARAMETERS[opcode]
        if n_params > 0:
            start = self.pointer + 1
            end = self.pointer + n_params + 1
            params = self.memory[start:end]
        else:
            params = []
        self.pointer += n_params + 1

        param_modes = self.get_parameter_modes(raw_param_modes, n_params)
        for i in range(n_params):
            if i == n_params - 1 and opcode in [1, 2, 3, 7, 8]:
                break
            if not param_modes[i]:  # position mode
                params[i] = self.memory[params[i]]

        return operation, params

    def get_parameter_modes(self, raw_param_modes: int,
                            n_params: int) -> List[bool]:
        param_modes = []
        for i in range(n_params):
            raw_param_modes, param_mode = divmod(raw_param_modes, 10)
            param_modes.append(bool(param_mode))
        return param_modes

    # OPERATIONS
    def add(self, p1: int, p2: int, loc: int) -> None:  # 1
        self.memory[loc] = p1 + p2

    def multiply(self, p1: int, p2: int, loc: int) -> None:  # 2
        self.memory[loc] = p1 * p2

    def take_input(self, loc: int) -> None:  # 3
        self.memory[loc] = next(self.input_values)

    def print_output(self, p1: int) -> None:  # 4
        self.output = p1

    def jump_if_true(self, p1: int, p2: int) -> None:  # 5
        if bool(p1):
            self.pointer = p2

    def jump_if_false(self, p1: int, p2: int) -> None:  # 6
        if not bool(p1):
            self.pointer = p2

    def less_than(self, p1: int, p2: int, loc: int) -> None:  # 7
        self.memory[loc] = 1 if p1 < p2 else 0

    def equals(self, p1: int, p2: int, loc: int) -> None:  # 8
        self.memory[loc] = 1 if p1 == p2 else 0

    def finish(self) -> None:  # 99
        self.is_finished = True


with open("input.txt") as input_file:
    memory = list(map(int, input_file.readline().split(",")))

max_output = 0
for permutation in itertools.permutations(range(5)):
    current_output = 0
    for phase_setting in permutation:
        solver = Solver(memory.copy(), [phase_setting, current_output])
        current_output = solver.solve()
    max_output = max(current_output, max_output)
print(max_output)
