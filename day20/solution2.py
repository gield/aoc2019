from collections import defaultdict
from heapq import heapify, heappop, heappush


def is_valid(x_new: int, y_new: int) -> bool:
    return 0 <= x_new < x_max and 0 <= y_new < y_max


def is_outer(x: int, y: int) -> bool:
    return x == 2 or x == x_max - 3 or y == 2 or y == y_max - 3


with open("input.txt") as f:
    raw_maze = [l[:-1] for l in f.readlines()]
y_max, x_max = len(raw_maze), len(raw_maze[0])

wind_directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
maze = defaultdict(set)
temp_teleports = {}
teleport_names = {}
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
                    teleport_names[x_tele, y_tele] = tele_name
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

todo = [(0, 0, source)]
heapify(todo)
seen = defaultdict(set)
seen[0] = {source}
is_found = False
while not is_found:
    cost, depth, point = heappop(todo)
    for reachable_point in maze[point]:
        if depth == 0 and reachable_point == target:
            print(cost + 1)
            is_found = True
            break
        if (point in teleport_names and reachable_point in teleport_names
                and teleport_names[point] == teleport_names[reachable_point]):
            new_depth = depth - 1 if is_outer(*point) else depth + 1
        else:
            new_depth = depth
        if new_depth < 0 or reachable_point in seen[new_depth]:
            continue
        seen[new_depth].add(reachable_point)
        heappush(todo, ((cost + 1, new_depth, reachable_point)))
