import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numList = ip.split(".", 4)
    if len(numList) < 4 or len(numList) > 4:
        return False
    for num in numList:
        try:
            if int(num) > 255:
                return False
        except ValueError:
            return False
    return True


if __name__ == "__main__":
    main()
