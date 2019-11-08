from os import path, remove
from classes import placeholder
import numpy as np

# Define the current level. Used for loading input/save output paths
CCC_LEVEL = 2
INPUT_FILE = 5

# Input/Output file path
SCRIPT_PATH = path.dirname(path.abspath(__file__))
INPUT = f"{SCRIPT_PATH}/../inputs/level{CCC_LEVEL}_{INPUT_FILE}.in"
OUTPUT = f"{SCRIPT_PATH}/../outputs/level{CCC_LEVEL}_{INPUT_FILE}.out"


def add_to_output(line: str) -> None:
    """Adds a line with the specified string to the problem output file."""
    with open(OUTPUT, "a+") as problem_output:
        problem_output.write(line + "\n")


if __name__ == "__main__":

        # Delete previous output file if it exists
        if path.exists(OUTPUT):
            remove(OUTPUT)

        size = []
        matrix = []

        with open(INPUT, "r") as problem_input:
            for n, line in enumerate(problem_input):
                if n == 0:
                    size = [int(a) for a in line.split(" ")]
                else:
                    matrix.append([int(i) for i in line.split(" ")][1::2])

        matrix = np.asarray(matrix)

        borders = [0 for i in range(np.max(matrix) + 1)]

        for y, row in enumerate(matrix):
            for x, value in enumerate(row):
                if x == 0 or y == 0 or x == size[1] - 1 or y == size[0] - 1:
                    borders[value] += 1
                else:
                    checks = [[1,0],[0,1],[-1,0],[0,-1]]
                    for diff in checks:
                        current_coords = np.add([x, y], diff)
                        if matrix[current_coords[1]][current_coords[0]] != value:
                            borders[value] += 1
                            break

        for country in borders:
            add_to_output(str(country))

        







