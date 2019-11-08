from os import path, remove
from classes import placeholder

# Define the current level. Used for loading input/save output paths
CCC_LEVEL = 1
INPUT_FILE = 1

# Input/Output file path
SCRIPT_PATH = path.dirname(path.abspath(__file__))
INPUT = f"{SCRIPT_PATH}/../level{CCC_LEVEL}_{INPUT_FILE}.in"
OUTPUT = f"{SCRIPT_PATH}/../level{CCC_LEVEL}_{INPUT_FILE}.out"


def add_to_output(line: str) -> None:
    """Adds a line with the specified string to the problem output file."""
    with open(OUTPUT, "a+") as problem_output:
        problem_output.write(line + "\n")


if __name__ == "__main__":

    # Delete previous output file if it exists
    if path.exists(OUTPUT):
        remove(OUTPUT)

    with open(INPUT, "r") as problem_input:
        for n, line in enumerate(problem_input):
            # Do stuff with the input
            pass
