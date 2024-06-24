def main():
    plate = input("Plate: ")
    t_f = is_valid(plate)
    if t_f == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if (
        start(plate) == True
        and length(plate) == True
        and punc(plate) == True
        and nums(plate) == True
    ):
        return True
    elif (
        start(plate) == False
        or length(plate) == False
        or punc(plate) == False
        or nums(plate) == False
    ):
        return False


# checks if first 2 chars are letters
def start(plate):

    if plate[0:2].isalpha() == True:
        return True

    else:
        return False


# checks if length is >= 2 and <= 6
def length(plate):

    if len(plate) >= 2 and len(plate) <= 6:
        return True

    else:
        return False


# checks if numbers are at the end, and first num != 0
def nums(plate):

    for i in range(0, len(plate)):
        if plate[i].isalpha() == False:
            location = plate.find(plate[i])
            if plate.find("0") == location:
                return False

            # checks if chars following the inital number are indeed numbers
            elif plate[location : len(plate)].isnumeric() == True:
                return True
            else:
                return False

    else:
        return True


# checks for spaces / puncuation
def punc(plate):

    if plate.isalnum() == True:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
