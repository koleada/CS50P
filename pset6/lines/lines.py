import sys

if len(sys.argv) < 2:
    exit("Too few command-line arguments")
if len(sys.argv) > 2:
    exit("Too many command-line arguments")

#
#
file = sys.argv[1]

if file[-3:] != ".py":
    exit("Not a Python file")

try:
    file = open(file, "r")
except FileNotFoundError:
    exit("File does not exist")
else:
    num_lines = 0
    for line in file:
        if len(line.rstrip().strip()) == 0 or line.strip().startswith("#") == True:
            pass
        else:
            num_lines = num_lines + 1
    print(num_lines)
