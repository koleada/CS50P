def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print(f"${val}")


def value(greeting):
    if greeting.strip().lower().find("hello") == 0:
        return 0

    elif greeting.lower().find("h") == 0:
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
