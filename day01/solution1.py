import math


def get_fuel(mass: int) -> int:
    return max(0, math.floor(mass / 3) - 2)


with open("input.txt", "r") as input_file:
    modules = map(int, input_file.readlines())
print(sum(map(get_fuel, modules)))
