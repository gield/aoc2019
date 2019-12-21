from collections import defaultdict
from heapq import heapify, heappop, heappush


def is_valid(x_new: int, y_new: int) -> bool:
    return 0 <= x_new < x_max and 0 <= y_new < y_max


with open("input.txt") as f:
    raw_maze = f.readlines()

wind_directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
y_max, x_max = len(raw_maze), len(raw_maze[0])
maze = defaultdict(set)
temp_teleports = {}
for y in range(y_max):
    for x in range(x_max):
        if raw_maze[y][x].isupper():
            for x_diff, y_diff in wind_directions:
                x_new, y_new = x + x_diff, y + y_diff
                if is_valid(x_new, y_new) and raw_maze[y_new][x_new].isupper():
                    x_tele, y_tele = x_new + x_diff, y_new + y_diff
                    if not (is_valid(x_tele, y_tele)
                            and raw_maze[y_tele][x_tele] == "."):
                        continue
                    if x_diff == 1 or y_diff == 1:
                        tele_name = raw_maze[y][x] + raw_maze[y_new][x_new]
                    else:  # reverse the portal name
                        tele_name = raw_maze[y_new][x_new] + raw_maze[y][x]
                    if tele_name == "AA":
                        source = (x_tele, y_tele)
                    elif tele_name == "ZZ":
                        target = (x_tele, y_tele)
                    elif tele_name in temp_teleports:
                        x_other, y_other = temp_teleports[tele_name]
                        maze[x_other, y_other].add((x_tele, y_tele))
                        maze[x_tele, y_tele].add((x_other, y_other))
                    else:
                        temp_teleports[tele_name] = (x_tele, y_tele)
        elif raw_maze[y][x] == ".":
            for x_diff, y_diff in wind_directions:
                x_new, y_new = x + x_diff, y + y_diff
                if is_valid(x_new, y_new) and raw_maze[y_new][x_new] == ".":
                    maze[x, y].add((x_new, y_new))

todo = [(0, source)]
heapify(todo)
seen = {source}
while target not in seen:
    cost, point = heappop(todo)
    for reachable_point in maze[point]:
        if reachable_point in seen:
            continue
        if reachable_point == target:
            print(cost + 1)
        seen.add(reachable_point)
        heappush(todo, ((cost + 1, reachable_point)))
