import itertools
import math


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm3(a: int, b: int, c: int) -> int:
    return lcm(lcm(a, b), c)


moons = [
    {"pos": [5, 4, 4], "vel": [0, 0, 0]},
    {"pos": [-11, -11, -3], "vel": [0, 0, 0]},
    {"pos": [0, 7, 0], "vel": [0, 0, 0]},
    {"pos": [-13, 2, 10], "vel": [0, 0, 0]},
]

per_axis = []
for axis in range(3):
    for step in itertools.count():
        for i in range(len(moons)):
            for j in range(len(moons)):
                if moons[i]["pos"][axis] > moons[j]["pos"][axis]:
                    moons[i]["vel"][axis] -= 1
                if moons[i]["pos"][axis] < moons[j]["pos"][axis]:
                    moons[i]["vel"][axis] += 1
        for i in range(len(moons)):
            moons[i]["pos"][axis] += moons[i]["vel"][axis]
        if all(moons[i]["vel"][axis] == 0 for i in range(len(moons))):
            per_axis.append(step + 1)
            break

print(lcm3(*per_axis) * 2)
