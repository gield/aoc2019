import numpy as np


def get_smallest_step(x_diff, y_diff):
    gcd = np.gcd(x_diff, y_diff)
    return x_diff // gcd, y_diff // gcd


def get_visible_asteroids(m, sx, sy):
    max_y, max_x = m.shape
    m[sy][sx] = "X"
    for y, x in zip(*np.where(m == "#")):
        x_diff, y_diff = get_smallest_step(x - sx, y - sy)
        x, y = x + x_diff, y + y_diff
        while x >= 0 and y >= 0 and x < max_x and y < max_y:
            if m[y][x] == "#":
                m[y][x] = "!"
            x, y = x + x_diff, y + y_diff
    return m


def get_best_asteroid(asteroid_map):
    highest_detected = 0
    for sy, sx in zip(*np.where(asteroid_map == "#")):
        visible_asteroids = get_visible_asteroids(asteroid_map.copy(), sx, sy)
        num_detected = (visible_asteroids == "#").sum()
        if num_detected > highest_detected:
            highest_detected = num_detected
            best_x, best_y = sx, sy
    return best_x, best_y, highest_detected


with open("input.txt", "r") as asteroid_map_file:
    raw_asteroid_map = asteroid_map_file.readlines()
asteroid_map = np.array([list(line.strip()) for line in raw_asteroid_map])
print(get_best_asteroid(asteroid_map)[2])
