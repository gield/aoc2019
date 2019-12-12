import math
from copy import deepcopy


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def lcm3(a, b, c):
    x = lcm(a, b)
    return lcm(x, c)


class Point:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def get_sum(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


moons = [
    {"pos": Point(5, 4, 4), "vel": Point(0, 0, 0)},
    {"pos": Point(-11, -11, -3), "vel": Point(0, 0, 0)},
    {"pos": Point(0, 7, 0), "vel": Point(0, 0, 0)},
    {"pos": Point(-13, 2, 10), "vel": Point(0, 0, 0)},
]

# moons = [
#     {"pos": Point(-1, 0, 2), "vel": Point(0, 0, 0)},
#     {"pos": Point(2, -10, -7), "vel": Point(0, 0, 0)},
#     {"pos": Point(4, -8, 8), "vel": Point(0, 0, 0)},
#     {"pos": Point(3, 5, -1), "vel": Point(0, 0, 0)},
# ]

# moons = [
#     {"pos": Point(-8, -10, 0), "vel": Point(0, 0, 0)},
#     {"pos": Point(5, 5, 10), "vel": Point(0, 0, 0)},
#     {"pos": Point(2, -7, 3), "vel": Point(0, 0, 0)},
#     {"pos": Point(9, -8, -3), "vel": Point(0, 0, 0)},
# ]

initial_moons = deepcopy(moons)

for step in range(100000000):
    for i in range(len(moons)):
        for j in range(len(moons)):
            if moons[i]["pos"].x > moons[j]["pos"].x: moons[i]["vel"].x -= 1
            if moons[i]["pos"].x < moons[j]["pos"].x: moons[i]["vel"].x += 1
    for i in range(len(moons)):
        moons[i]["pos"].x += moons[i]["vel"].x
    # if all(moons[i]["pos"].x == initial_moons[i]["pos"].x for i in range(len(moons))):
    #     best_x = step + 1
    #     break
    if all(moons[i]["vel"].x == 0 for i in range(len(moons))):
        best_x = step + 1
        break

for step in range(100000000):
    for i in range(len(moons)):
        for j in range(len(moons)):
            if moons[i]["pos"].y > moons[j]["pos"].y: moons[i]["vel"].y -= 1
            if moons[i]["pos"].y < moons[j]["pos"].y: moons[i]["vel"].y += 1
    for i in range(len(moons)):
        moons[i]["pos"].y += moons[i]["vel"].y
    # if all(moons[i]["pos"].y == initial_moons[i]["pos"].y for i in range(len(moons))):
    #     best_y = step + 1
    #     break
    if all(moons[i]["vel"].y == 0 for i in range(len(moons))):
        best_y = step + 1
        break

for step in range(100000000):
    for i in range(len(moons)):
        for j in range(len(moons)):
            if moons[i]["pos"].z > moons[j]["pos"].z: moons[i]["vel"].z -= 1
            if moons[i]["pos"].z < moons[j]["pos"].z: moons[i]["vel"].z += 1
    for i in range(len(moons)):
        moons[i]["pos"].z += moons[i]["vel"].z
    # if all(moons[i]["pos"].z == initial_moons[i]["pos"].z for i in range(len(moons))):
    #     best_z = step + 1
    #     break
    if all(moons[i]["vel"].z == 0 for i in range(len(moons))):
        best_z = step + 1
        break

print(lcm3(best_x, best_y, best_z))
print(lcm3(best_x, best_y, best_z) * 2)