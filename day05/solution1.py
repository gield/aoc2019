from typing import Any, List, Tuple


class Solver:

    def __init__(self, memory: List[int], input_value: int):
        self.memory = memory
        self.pointer = 0
        self.is_finished = False
        self.input_value = input_value

        self.OPERATIONS = {
            1: self.add,
            2: self.multiply,
            3: self.take_input,
            4: self.print_output,
            99: self.finish,
        }
        self.NUMBER_OF_PARAMETERS = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            99: 0,
        }

    def solve(self):
        while not self.is_finished:
            self.step()

    def step(self):
        operation, params = self.read_instruction()
        operation(*params)

    def read_instruction(self) -> Tuple[Any, List[int]]:
        instruction = self.memory[self.pointer]
        raw_param_modes, opcode = divmod(instruction, 100)
        operation = self.OPERATIONS[opcode]
        n_params = self.NUMBER_OF_PARAMETERS[opcode]
        if n_params > 0:
            start = self.pointer + 1
            end = self.pointer + n_params + 1
            params = self.memory[start:end]
        else:
            params = []
        # print(instruction, params)
        self.pointer += n_params + 1

        param_modes = self.get_parameter_modes(raw_param_modes, n_params)
        for i in range(n_params):
            if i == n_params - 1 and opcode in [1, 2, 3]:
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
    def add(self, p1: int, p2: int, loc: int):  # 1
        self.memory[loc] = p1 + p2

    def multiply(self, p1: int, p2: int, loc: int):  # 2
        self.memory[loc] = p1 * p2

    def take_input(self, loc: int):  # 3
        self.memory[loc] = self.input_value

    def print_output(self, p1: int):  # 4
        print(p1)

    def finish(self):  # 99
        self.is_finished = True


with open("input.txt") as input_file:
    memory = list(map(int, input_file.readline().split(",")))

solver = Solver(memory, 1)
solver.solve()
