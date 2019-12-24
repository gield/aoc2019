from collections import defaultdict


def get_biodiversity_rating(area):
    return sum(2 ** (5 * y + x)
               for y in range(5) for x in range(5)
               if area[x, y] == "#")


def evolve(area):
    new_area = defaultdict(lambda: ".")
    for y in range(5):
        for x in range(5):
            num_bugs_around_tile = get_num_bugs_around_tile(area, x, y)
            if area[x, y] == "#" and num_bugs_around_tile == 1:
                new_area[x, y] = "#"
            elif area[x, y] == "." and num_bugs_around_tile in {1, 2}:
                new_area[x, y] = "#"
            else:
                new_area[x, y] = "."
    return new_area

def get_num_bugs_around_tile(area, x, y):
    num_bugs = 0
    for x_diff, y_diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x_new, y_new = x + x_diff, y + y_diff
        if area[x_new, y_new] == "#":
            num_bugs += 1
    return num_bugs


def print_area(area):
    for y in range(5):
        for x in range(5):
            print(area[x, y], end="")
        print()


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
# lines = """
# ....#
# #..#.
# #..##
# ..#..
# #...."""[1:].splitlines()

area = defaultdict(lambda: ".")
for y, line in enumerate(lines):
    for x, char in enumerate(list(line)):
        area[x, y] = char

biodiversity_ratings = set()
biodiversity_ratings.add(get_biodiversity_rating(area))
all_areas = set()
while True:
    area = evolve(area)
    rating = get_biodiversity_rating(area)
    if rating in biodiversity_ratings:
        print(rating)
        break
    biodiversity_ratings.add(rating)
