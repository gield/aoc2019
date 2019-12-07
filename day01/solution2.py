import math


def get_fuel(mass: int) -> int:
    return max(0, math.floor(mass / 3) - 2)


def get_all_fuel(mass: int) -> int:
    total_fuel = 0
    while (mass := get_fuel(mass)) > 0:
        total_fuel += mass
    return total_fuel


with open("input.txt", "r") as input_file:
    modules = map(int, input_file.readlines())
print(sum(map(get_all_fuel, modules)))
