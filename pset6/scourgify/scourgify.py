import sys
import csv

if len(sys.argv) < 3:
    exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    exit("Too many command-line arguments")
else:
    before = sys.argv[1]
    after = sys.argv[2]

    try:
        before = open(before, "r")
    except FileNotFoundError:
        exit(f"Could not read {sys.argv[1]}")
    else:
        after = open(after, "w+")
        reader = csv.reader(before)
        for row in reader:
            name, house = row[0].strip(), row[1].strip()
            if name.find(",") > 0:
                name = name.split(",", 2)
                first, last = name[1].strip(), name[0].strip()
                after.write(f"{first},{last},{house}\n")
            else:
                after.write("first,last,house\n")
