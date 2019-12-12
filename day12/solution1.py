moons = [
    {"pos": [5, 4, 4], "vel": [0, 0, 0]},
    {"pos": [-11, -11, -3], "vel": [0, 0, 0]},
    {"pos": [0, 7, 0], "vel": [0, 0, 0]},
    {"pos": [-13, 2, 10], "vel": [0, 0, 0]},
]

for step in range(1000):
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            for axis in range(3):
                if moons[j]["pos"][axis] < moons[i]["pos"][axis]:
                    moons[i]["vel"][axis] -= 1
                    moons[j]["vel"][axis] += 1
                if moons[j]["pos"][axis] > moons[i]["pos"][axis]:
                    moons[i]["vel"][axis] += 1
                    moons[j]["vel"][axis] -= 1
    for i in range(len(moons)):
        for axis in range(3):
            moons[i]["pos"][axis] += moons[i]["vel"][axis]
    
sum_total_energy = sum(sum(map(abs, moon["pos"])) * sum(map(abs, moon["vel"]))
                       for moon in moons)
print(sum_total_energy)
