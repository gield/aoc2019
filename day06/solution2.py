from typing import Set


def get_distance(from_obj: str, to_obj: str) -> int:
    distance_counter = 0
    while from_obj in orbit_dict and from_obj != to_obj:
        from_obj = orbit_dict[from_obj]
        distance_counter += 1
    return distance_counter


def get_parents(obj: str) -> Set[str]:
    parents = set()
    while obj in orbit_dict:
        obj = orbit_dict[obj]
        parents.add(obj)
    return parents


with open("input.txt", "r") as orbit_txt:
    orbit_map = map(str.strip, orbit_txt.readlines())

orbit_dict = dict()
all_objects = set()
for orbit in orbit_map:
    object1, object2 = orbit.split(")")
    orbit_dict[object2] = object1
    all_objects.update([object1, object2])

your_parents = get_parents("YOU")
santas_parents = get_parents("SAN")
min_distance = float("inf")
for parent in your_parents & santas_parents:
    distance = get_distance("YOU", parent) + get_distance("SAN", parent)
    if distance < min_distance:
        min_distance = distance
print(min_distance - 2)
