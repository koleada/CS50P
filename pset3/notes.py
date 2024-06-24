# great way to check user input and keep prompting until the input is valid

def main():

    x=get_int("Whats x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:

        try:
            return int(input(prompt))
        except ValueError:
            pass

main()