with open("input.txt", "r") as orbit_txt:
    orbit_map = map(str.strip, orbit_txt.readlines())

orbit_dict = dict()
all_objects = set()
for orbit in orbit_map:
    object1, object2 = orbit.split(")")
    orbit_dict[object2] = object1
    all_objects.update([object1, object2])

counter = 0
for obj in all_objects:
    while obj in orbit_dict:
        obj = orbit_dict[obj]
        counter += 1
print(counter)
