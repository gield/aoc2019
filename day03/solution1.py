from typing import Set


class Coordinate:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def move(self, direction: str) -> 'Coordinate':
        if direction == "R":
            return Coordinate(self.x + 1, self.y)
        elif direction == "L":
            return Coordinate(self.x - 1, self.y)
        elif direction == "U":
            return Coordinate(self.x, self.y + 1)
        elif direction == "D":
            return Coordinate(self.x, self.y - 1)
        else:
            raise ValueError(f"The given direction {direction}is not valid.")


def manhattan(coord: Coordinate) -> int:
    return abs(coord.x) + abs(coord.y)


def get_wire_coordinates(path: str) -> Set[Coordinate]:
    current_coordinate = Coordinate(0, 0)
    all_coordinates = set()
    for direction in path.split(","):
        size = int(direction[1:])
        for _ in range(size):
            current_coordinate = current_coordinate.move(direction[0])
            all_coordinates.add(current_coordinate)
    return all_coordinates


with open("input.txt", "r") as input_file:
    wire1_path = input_file.readline()
    wire2_path = input_file.readline()

wire1_coordinates = get_wire_coordinates(wire1_path)
wire2_coordinates = get_wire_coordinates(wire2_path)

intersection_coordinates = wire1_coordinates & wire2_coordinates
print(min(map(manhattan, intersection_coordinates)))
