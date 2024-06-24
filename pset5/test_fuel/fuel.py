def main():
    while True:
        frac = input("Fraction: ")
        try:
            percent = convert(frac)
        except (TypeError, ValueError, ZeroDivisionError):
            pass
        else:
            if percent != None:
                break
            else:
                pass

    print(gauge(percent))


def convert(fraction):

    x, y = fraction.split("/", 2)

    if not (x.isdigit() or y.isdigit()):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        result = int(round((int(x) / int(y)) * 100, 0))
        if result > 100:
            raise ValueError
        else:

            return result


def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
