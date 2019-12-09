import itertools
from enum import IntEnum
from typing import Any, List, Tuple


class ParameterMode(IntEnum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    RELATIVE_MODE = 2


class Solver:

    def __init__(self, memory: List[int], input_values: List[int]) -> None:
        self.memory = memory
        self.input_values = iter(input_values)
        self.output = []
        self.pointer = 0
        self.relative_base = 0
        self.is_finished = False

        self.OPERATIONS = {
            # opcode: (operation, n_params, last_param_is_loc)
            1: (self.add, 3, True),
            2: (self.multiply, 3, True),
            3: (self.take_input, 1, True),
            4: (self.print_output, 1, False),
            5: (self.jump_if_true, 2, False),
            6: (self.jump_if_false, 2, False),
            7: (self.less_than, 3, True),
            8: (self.equals, 3, True),
            9: (self.adjust_relative_base, 1, False),
            99: (self.finish, 0, False),
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
        operation, n_params, last_param_is_loc = self.OPERATIONS[opcode]
        params = self.memory[self.pointer + 1:self.pointer + n_params + 1]
        param_modes = self.get_parameter_modes(raw_param_modes, n_params)
        params = self.convert_params(params, param_modes, last_param_is_loc)
        self.pointer += n_params + 1
        return operation, params

    def get_parameter_modes(self, raw_param_modes: int,
                            n_params: int) -> List[ParameterMode]:
        param_modes = []
        for i in range(n_params):
            raw_param_modes, param_mode = divmod(raw_param_modes, 10)
            param_modes.append(ParameterMode(param_mode))
        return param_modes

    def convert_params(self, params: List[int],
                       param_modes: List[ParameterMode],
                       last_param_is_loc: bool) -> List[int]:
        n_params = len(params)
        for i in range(n_params):
            if last_param_is_loc and i == n_params - 1:
                if param_modes[i] == ParameterMode.RELATIVE_MODE:
                    params[i] += self.relative_base
            elif param_modes[i] != ParameterMode.IMMEDIATE_MODE:
                loc = params[i]
                if param_modes[i] == ParameterMode.RELATIVE_MODE:
                    loc += self.relative_base
                self.increase_memory_size(loc)
                params[i] = self.memory[loc]
        return params

    def increase_memory_size(self, last_loc):
        if last_loc >= len(self.memory):
            extension = [0] * (last_loc + 1 - len(self.memory))
            self.memory.extend(extension)

    # OPERATIONS
    def add(self, p1: int, p2: int, loc: int) -> None:  # 1
        self.increase_memory_size(loc)
        self.memory[loc] = p1 + p2

    def multiply(self, p1: int, p2: int, loc: int) -> None:  # 2
        self.increase_memory_size(loc)
        self.memory[loc] = p1 * p2

    def take_input(self, loc: int) -> None:  # 3
        self.increase_memory_size(loc)
        self.memory[loc] = next(self.input_values)

    def print_output(self, p1: int) -> None:  # 4
        self.output.append(p1)

    def jump_if_true(self, p1: int, p2: int) -> None:  # 5
        if bool(p1):
            self.pointer = p2

    def jump_if_false(self, p1: int, p2: int) -> None:  # 6
        if not bool(p1):
            self.pointer = p2

    def less_than(self, p1: int, p2: int, loc: int) -> None:  # 7
        self.increase_memory_size(loc)
        self.memory[loc] = 1 if p1 < p2 else 0

    def equals(self, p1: int, p2: int, loc: int) -> None:  # 8
        self.increase_memory_size(loc)
        self.memory[loc] = 1 if p1 == p2 else 0

    def adjust_relative_base(self, p1: int) -> None:  # 9
        self.relative_base += p1

    def finish(self) -> None:  # 99
        self.is_finished = True


with open("input.txt") as input_file:
    memory = list(map(int, input_file.readline().split(",")))

solver = Solver(memory, input_values=[1])
output = solver.solve()
print(output[0])
