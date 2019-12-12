import itertools
import math


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


moons = [
    {"pos": [5, 4, 4], "vel": [0, 0, 0]},
    {"pos": [-11, -11, -3], "vel": [0, 0, 0]},
    {"pos": [0, 7, 0], "vel": [0, 0, 0]},
    {"pos": [-13, 2, 10], "vel": [0, 0, 0]},
]

steps_per_period = []
for axis in range(3):
    positions = [m["pos"][axis] for m in moons]
    velocities = [m["vel"][axis] for m in moons]
    initial_positions = positions.copy()
    initial_velocities = velocities.copy()
    for step in itertools.count():
        for i in range(len(moons)):
            for j in range(i + 1, len(moons)):
                if positions[i] > positions[j]:
                    velocities[i] -= 1
                    velocities[j] += 1
                if positions[i] < positions[j]:
                    velocities[i] += 1
                    velocities[j] -= 1
        for i in range(len(moons)):
            positions[i] += velocities[i]
        if positions == initial_positions and velocities == initial_velocities:
            steps_per_period.append(step + 1)
            break

steps_axis1, steps_axis2, steps_axis3 = steps_per_period
print(lcm(steps_axis1, lcm(steps_axis2, steps_axis3)))
