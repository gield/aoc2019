import numpy as np
from heapq import heapify, heappop, heappush


def is_walkable(char: str) -> bool:
    return char == "." or char == "@" or (char.isalpha() and char.islower())


memo = {}
def get_shortest_path(vault, door_locations, p1, p2):
    hashed_vault = ("".join(sorted(door_locations.keys())), p1, p2)
    if hashed_vault in memo:
        return memo[hashed_vault]
    visited = {p1}
    todo = [(0, p1, [])]
    heapify(todo)
    while todo:
        cost, p_old, path_old = heappop(todo)
        for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p_new = p_old[0] + x_diff, p_old[1] + y_diff
            path_new = path_old + [p_new]
            if p_new == p2:
                memo[hashed_vault] = path_new
                return path_new
            if p_new not in visited and is_walkable(vault[p_new]):
                visited.add(p_new)
                heappush(todo, (cost + 1, p_new, path_new))
    memo[hashed_vault] = []
    return []


min_score = float('inf')
def dfs(vault, key_locations, door_locations, p_player, num_steps, unlocked_keys):
    global min_score
    if num_steps > min_score:
        return float('inf')
    if not key_locations:  # We have a solution
        if num_steps < min_score:  # We have a better solution
            min_score = num_steps
        return num_steps

    reachable = [(get_shortest_path(vault, door_locations, p_player, p), p)
                for p in key_locations.values()]
    reachable = [(path, p) for path, p in reachable if len(path)]
    reachable.sort(key=lambda t: len(t[0]))
    if len(reachable) == 0:
        return float('inf')
    elif len(reachable) > 1:
        for path1, p1 in reachable:
            for path2, p2 in reachable:
                if p1 == p2:
                    continue
                if p1 in path2:
                    del reachable[reachable.index((path2, p2))]
    scores = []
    for path, p_key in reachable:
        if num_steps + len(path) >= min_score:
            continue
        temp_vault = vault.copy()
        temp_key_locations = key_locations.copy()
        temp_door_locations = door_locations.copy()

        key = temp_vault[p_key]
        temp_vault[p_key] = "."
        del temp_key_locations[key]
        if key.upper() in temp_door_locations:
            p_door = temp_door_locations.pop(key.upper())
            temp_vault[p_door] = "."
        temp_vault[p_player] = "."
        temp_vault[p_key] = "@"
        score = dfs(temp_vault, temp_key_locations, temp_door_locations,
                    p_key, num_steps + len(path), unlocked_keys + [key])
        scores.append(score)
    return min(scores) if scores else float('inf')


with open("input.txt", "r") as f:
    raw_vault = list(map(str.strip, f.readlines()))

max_y, max_x = len(raw_vault), len(raw_vault[0])
vault = np.array([list(line) for line in raw_vault]).T
key_locations = {}
door_locations = {}
for y in range(vault.shape[1]):
    for x in range(vault.shape[0]):
        char = vault[x, y]
        if char == "@":
            p_player = x, y
        elif char.isalpha():
            if char.islower():
                key_locations[char] = x, y
            else:
                door_locations[char] = x, y

print(dfs(vault, key_locations, door_locations, p_player, 0, []))
