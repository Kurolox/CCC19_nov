from os import path, remove
from classes import placeholder
import numpy

# Define the current level. Used for loading input/save output paths
CCC_LEVEL = 1
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
                    matrix.append([int(i) for i in line.split(" ")])

        matrix = numpy.asarray(matrix)
        min_val = numpy.min(matrix)
        max_val = numpy.max(matrix)
        mean_val = numpy.mean(matrix)

        output = f"{min_val} {max_val} {int(numpy.floor(mean_val))}"
        add_to_output(output)




