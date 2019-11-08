from os import path, remove
from classes import placeholder
import numpy as np
from scipy import ndimage
from scipy.spatial import distance
import sys
# Define the current level. Used for loading input/save output paths
CCC_LEVEL = 3
INPUT_FILE = 5

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

    size = []
    matrix = []
    capitals = []

    with open(INPUT, "r") as problem_input:
        for n, line in enumerate(problem_input):
            if n == 0:
                size = [int(a) for a in line.split(" ")]
            else:
                matrix.append([int(i) for i in line.split(" ")][1::2])

    matrix = np.asarray(matrix)

    country_amount = np.max(matrix) + 1

    borders = [0 for i in range(country_amount)]

    for country in range(country_amount):
        isolated_map = np.where(matrix == country, 1, 0)
        center_of_mass = [int(np.floor(a))
                          for a in ndimage.measurements.center_of_mass(isolated_map)][::-1]

        if is_inner(isolated_map, size, *center_of_mass):
            capitals.append(center_of_mass)
        else:

            # Modified clone to get only valid capital points

            valid_points = np.where(isolated_map == 1)
            country_coordinates = np.array(valid_points).T

            kill_me = np.asarray([[distance.euclidean((i, j),center_of_mass) if is_inner(isolated_map, size, i, j)
                               else float("inf") for i in range(size[1])] for j in range(size[0])])

            
            capitals.append(np.unravel_index(np.argmin(kill_me, axis=None), kill_me.shape)[::-1])








            """valid_coordinates=[]
            #valid_points = [[10 for i in range(len(valid_points))] for j in range(len(valid_points[0]))]
            for point in valid_points:
                if(is_inner(isolated_map,size,point[1],point[0])): 
                    valid_coordinates.push(point)
            print(valid_coordina tes)"""

    for capital in capitals:
        add_to_output(str(f"{capital[0]} {capital[1]}"))
