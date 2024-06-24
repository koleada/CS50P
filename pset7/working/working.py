import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if s.lower().find("to") < 0:
        raise ValueError

    time_list = s.lower().split("to", 2)

    first = time_list[0].split()
    second = time_list[1].split()

    if first[0].find(":") > 0:
        first_time = first[0].split(":")
        second_time = second[0].split(":")
        if int(first_time[0]) > 12 or int(second_time[0]) > 12:
            raise ValueError
        elif int(first_time[1]) > 59 or int(second_time[1]) > 59:
            raise ValueError
        else:
            if int(second_time[0]) == 12:
                if second[1].strip().lower() == "pm":
                    second_time[0] = 12
                else:
                    second_time[0] = 0
            elif second[1].strip().lower() == "pm":
                second_time[0] = (int(second_time[0])) + 12

            if int(first_time[0]) == 12:
                if first[1].strip().lower() == "pm":
                    first_time[0] = 12
                else:
                    first_time[0] = 0
            elif first[1].strip().lower() == "pm":
                first_time[0] = int(first_time[0]) + 12
            return f"{str(first_time[0]).zfill(2)}:{first_time[1]} to {str(second_time[0]).zfill(2)}:{second_time[1]}"

    else:
        if int(first[0]) > 12 or int(second[0]) > 12:
            raise ValueError
        else:

            if int(second[0]) == 12:
                if second[1].strip().lower() == "pm":
                    second[0] = 12
                else:
                    second[0] = 0
            elif second[1].strip().lower() == "pm" and second[0] != 12:
                second[0] = (int(second[0])) + 12

            if int(first[0]) == 12:
                if first[1].strip().lower() == "pm":
                    first[0] = 12
                else:
                    first[0] = 0
            elif first[1].strip().lower() == "pm" and first[0] != 12:
                first[0] = int(first[0]) + 12
            return f"{str(first[0]).zfill(2)}:00 to {str(second[0]).zfill(2)}:00"


if __name__ == "__main__":
    main()
