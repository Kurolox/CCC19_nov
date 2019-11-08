from os import path, remove
from classes import placeholder
import numpy as np
from scipy import ndimage
from scipy.spatial import distance
import sys
# Define the current level. Used for loading input/save output paths
CCC_LEVEL = 4
INPUT_FILE = "example"

# Input/Output file path
SCRIPT_PATH = path.dirname(path.abspath(__file__))
INPUT = f"{SCRIPT_PATH}/../inputs/level{CCC_LEVEL}_{INPUT_FILE}.in"
OUTPUT = f"{SCRIPT_PATH}/../outputs/level{CCC_LEVEL}_{INPUT_FILE}.out"


def add_to_output(line: str) -> None:
    """Adds a line with the specified string to the problem output file."""
    with open(OUTPUT, "a+") as problem_output:
        problem_output.write(line + "\n")


def is_inner(matrix, size, x, y):
    if x == 0 or y == 0 or x == size[1] - 1 or y == size[0] - 1:
        return False
    else:
        checks = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for diff in checks:
            current_coords = np.add([x, y], diff)
            if matrix[current_coords[1]][current_coords[0]] != 1:
                return False
    return True


if __name__ == "__main__":

        # Delete previous output file if it exists
    if path.exists(OUTPUT):
        remove(OUTPUT)

    ray_amount = 0

    with open(INPUT, "r") as problem_input:
        for n, line in enumerate(problem_input):
            if n == 0:
                size = [int(a) for a in line.split(" ")]
            elif n == 1:
                ray_amount = int(line)
            else:
                ray_info = [int(a) for a in line.split(" ")]
                ray_origin = ray_info[:2]
                ray_direction = ray_info[2:]

                points = [*ray_origin]

                add_to_output(f"{' '.join([str(a) for a in points])}")