import random


def main():
    level = get_level()

    correct = 0
    outer_counter = 0
    while outer_counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        inner_counter = 0

        while True:
            print(f"{x} + {y} = ", end="")
            try:
                guess = int(input())
            except ValueError:
                print("EEE")
                inner_counter = inner_counter + 1
                pass
            answer = x + y
            if guess == answer:
                inner_counter = 3
                outer_counter = outer_counter + 1
                correct = correct + 1
                break
            else:
                if inner_counter != 2:
                    inner_counter = inner_counter + 1
                    print("EEE")
                    pass
                else:
                    print(f"{x} + {y} = {answer}")
                    outer_counter = outer_counter + 1
                    break

    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level != 1 and level != 2 and level != 3:
                pass
            else:
                return level


def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
        return num
    elif level == 2:
        num = random.randint(10, 99)
        return num
    else:
        num = random.randint(100, 999)
        return num


if __name__ == "__main__":
    main()
