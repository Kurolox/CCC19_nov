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


def calc_endpoint(size, ray_origin, ray_direction):
    while True:
        ray_origin = np.add(ray_direction, ray_origin)

        if ray_origin[0] <= 0 or ray_origin[1] <= 0 or ray_origin[0] >= size[1] - 1 or ray_origin[1] >= size[0] - 1:
            return ray_origin


def is_inside(size, point):

    if point[0] < 0 or point[1] < 0 or point[0] > size[1] - 1 or point[1] > size[0] - 1:
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

                mess_point_interval = [i/2 for i in ray_direction]
                # Continue Here

                coord_a = ray_origin
                coord_b = calc_endpoint(size, ray_origin, ray_direction)

                calc_range = np.linspace(0, 1, 1001)
                solutions = [ray_origin]

                for i, ratio in enumerate(calc_range):
                    distance_x = ((coord_b[0] - coord_a[0])
                                  * ratio) + coord_a[0]
                    distance_y = ((coord_b[1] - coord_a[1])
                                  * ratio) + coord_a[1]

                    endpoint = [int(round(distance_x)), int(round(distance_y))]

                    
                    previous_endpoint = solutions[-1]

                    if endpoint[0] != previous_endpoint[0] and endpoint[1] != previous_endpoint[1]:

                        missing_point_1 = [endpoint[0], previous_endpoint[1]]
                        missing_point_2 = [previous_endpoint[0], endpoint[1]]
                        
                        # Skipped midpoints, calc intervals
                        if abs(ray_direction[0]) >= abs(ray_direction[1]):
                            #if missing_point_1[0] > missing_point_2[0]:
                            solutions.append(missing_point_1)
                            solutions.append(missing_point_2)

                        else:
                            solutions.append(missing_point_2)
                            solutions.append(missing_point_1)

                    if endpoint not in solutions:
                        solutions.append(endpoint)

                solutions = [
                    solution for solution in solutions if is_inside(size, solution)]
                # End here

                add_to_output(
                    f"{' '.join([str(' '.join([str(i) for i in a])) for a in solutions])}")
