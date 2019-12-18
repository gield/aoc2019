import numpy as np
from collections import defaultdict
from heapq import heapify, heappop, heappush


def get_possible_routes(vault, p_source):
    # From some position (i.e. a key or the entrance), how much does it cost to
    # get to every key? Also include all points of interest (i.e. keys or
    # doors) encountered on that route as interesting information.
    possible_routes = {}
    visited = {p_source}
    todo = [(0, p_source, "")]
    heapify(todo)
    while todo:
        cost, p_old, points_of_interest = heappop(todo)
        if vault[p_old] not in "#.@" and cost > 0:
            possible_routes[vault[p_old]] = (cost, points_of_interest)
            points_of_interest += vault[p_old]
        for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p_new = p_old[0] + x_diff, p_old[1] + y_diff
            if p_new not in visited and vault[p_new] not in "#":
                visited.add(p_new)
                heappush(todo, (cost + 1, p_new, points_of_interest))
    return possible_routes


def get_all_routes(vault):
    # For all interesting positions (i.e. keys and the entrance), get all
    # possible routes.
    all_routes = {}
    for y in range(vault.shape[1]):
        for x in range(vault.shape[0]):
            if vault[x, y] not in "#.":
                all_routes[vault[x, y]] = get_possible_routes(vault, (x, y))
    return all_routes


def dfs(location, num_steps, unlocked_keys):
    global min_score
    if num_steps > min_score:
        return float('inf')
    if len(unlocked_keys) == len(all_keys):  # We have a solution
        if num_steps < min_score:  # We have a better solution
            min_score = num_steps
        return num_steps

    scores = []
    for key in all_keys - unlocked_keys:
        cost, points_of_interest = all_routes[location][key]
        if num_steps + cost >= min_score:
            continue
        is_reachable = all(k in unlocked_keys or k.lower() in unlocked_keys
                           for k in points_of_interest)
        if is_reachable:
            temp_unlocked_keys = unlocked_keys | {key}
            score = dfs(key, num_steps + cost, temp_unlocked_keys)
            scores.append(score)
    return min(scores) if scores else float('inf')


with open("input.txt", "r") as f:
    raw_vault = list(map(str.strip, f.readlines()))

max_y, max_x = len(raw_vault), len(raw_vault[0])
vault = np.array([list(line) for line in raw_vault]).T
all_keys = {vault[x, y]
            for y in range(vault.shape[1]) for x in range(vault.shape[0])
            if vault[x, y].islower()}
all_routes = get_all_routes(vault)

min_score = float('inf')
print(dfs("@", 0, set()))
