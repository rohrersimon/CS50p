import sys
from os import path

def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line != '' and not stripped_line.startswith('#'):
            count += 1

    return count


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not path.exists(filename):
    sys.exit("File does not exist")
elif not filename.endswith('.py'):
    sys.exit("Not a pyton file")

print(count_lines(filename))