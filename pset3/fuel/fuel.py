def main():

    x,y = fuel()

    percent = int(round((int(x)/int(y))*100, 0))

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")

def fuel():
    while True:

        try:
            x,y = input("Fraction: ").split("/", 2)
            while (int(x) / int(y) > 1.0):
                x,y = input("Fraction: ").split("/", 2)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return (int(x),  int(y))
main()

