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
            if p_new not in visited and vault[p_new] != "#":
                visited.add(p_new)
                heappush(todo, (cost + 1, p_new, points_of_interest))
    return possible_routes


def get_all_routes(vault):
    # For all interesting positions (i.e. keys and the entrance), get all
    # possible routes.
    all_routes = {}
    for y in range(vault.shape[1]):
        for x in range(vault.shape[0]):
            if vault[x, y] not in "#." and not vault[x, y].isupper():
                all_routes[vault[x, y]] = get_possible_routes(vault, (x, y))
    return all_routes


def is_reachable(unlocked_keys, points_of_interest):
    return all(k in unlocked_keys or k.lower() in unlocked_keys
               for k in points_of_interest)


with open("input.txt", "r") as f:
    raw_vault = list(map(str.strip, f.readlines()))
vault = np.array([list(line) for line in raw_vault]).T  # Use (x,y), not (y,x)

all_keys = {vault[x, y]
            for y in range(vault.shape[1]) for x in range(vault.shape[0])
            if vault[x, y].islower()}
all_routes = get_all_routes(vault)

# Keep track of current location, the keys found up until now, and the cost
previous_state = defaultdict(lambda: float('inf'))
previous_state.update({("@", ""): 0})
# Find the keys iteratively using BFS
for _ in range(len(all_keys)):
    cur_state = defaultdict(lambda: float('inf'))
    for (location, unlocked_keys_str), num_steps in previous_state.items():
        unlocked_keys = set(unlocked_keys_str)
        for key in all_keys - unlocked_keys:
            cost, points_of_interest = all_routes[location][key]
            if is_reachable(unlocked_keys, points_of_interest):
                unlocked_keys_str = "".join(sorted(unlocked_keys | {key}))
                new_cost = num_steps + cost
                if new_cost < cur_state[key, unlocked_keys_str]:
                    cur_state[key, unlocked_keys_str] = new_cost
    previous_state = cur_state

print(min(previous_state.values()))
