from typing import List


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


def get_wire_coordinates(path: str) -> List[Coordinate]:
    current_coordinate = Coordinate(0, 0)
    all_coordinates = []
    for direction in path.split(","):
        size = int(direction[1:])
        for _ in range(size):
            current_coordinate = current_coordinate.move(direction[0])
            all_coordinates.append(current_coordinate)
    return all_coordinates


def num_steps(wire1_coords: List[Coordinate], wire2_coords: List[Coordinate],
              intersect: Coordinate) -> int:
    return wire1_coords.index(intersect) + wire2_coords.index(intersect) + 2


with open("input.txt", "r") as input_file:
    wire1_path = input_file.readline()
    wire2_path = input_file.readline()

wire1_coordinates = get_wire_coordinates(wire1_path)
wire2_coordinates = get_wire_coordinates(wire2_path)

intersection_coordinates = set(wire1_coordinates) & set(wire2_coordinates)
number_of_steps = [num_steps(wire1_coordinates, wire2_coordinates, intersect)
                   for intersect in intersection_coordinates]
print(min(number_of_steps))
