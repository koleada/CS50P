import sys
import tabulate

if len(sys.argv) < 2:
    exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    exit("Too many command-line arguments")
else:
    file = sys.argv[1]

    if file[-4:] != ".csv":
        exit("Not a CSV file")

    else:
        try:
            file = open(file, "r")
        except FileNotFoundError:
            exit("File does not exist")
        else:
            pizzas = []
            for line in file:
                type, small, large = line.rstrip().split(",")
                pizza = [type, small, large]
                pizzas.append(pizza)

            print(tabulate.tabulate(pizzas, headers="firstrow", tablefmt="grid"))
