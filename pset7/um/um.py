import re


def main():
    print(count(input("Text: ")))


def count(input):
    input = input.split()
    counter = 0
    for word in input:
        if re.search(r"^um(?:\W*)", word, re.IGNORECASE):
            if str(word).startswith("umm") > 0:
                pass
            else:
                counter = counter + 1
    return counter


if __name__ == "__main__":
    main()
