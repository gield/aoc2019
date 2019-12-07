from typing import List


def run_program(int_code_list: List[int]) -> List[int]:
    for i in range(0, len(int_code_list), 4):
        opcode = int_code_list[i]
        if opcode == 99:
            break
        p1, p2, p3 = int_code_list[i+1:i+4]  # get next 3 addresses -> params
        if opcode == 1:
            int_code_list[p3] = int_code_list[p1] + int_code_list[p2]
        elif opcode == 2:
            int_code_list[p3] = int_code_list[p1] * int_code_list[p2]
    return int_code_list


with open("input.txt") as input_file:
    original_int_code_list = list(map(int, input_file.readline().split(",")))

for i in range(100):
    for j in range(100):
        int_code_list = original_int_code_list.copy()
        int_code_list[1] = i
        int_code_list[2] = j
        output = run_program(int_code_list)
        if output[0] == 19690720:
            print(100 * i + j)
