import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    content_list = html.split()

    for piece in content_list:
        if matches := re.search(
            # the ?: tells compiler this group does not have to be captured thus the total # of groups is less
            r"^.+(https?://)(?:www\.)?youtube\.com/(?:embed/)(.+)(\")",
            piece,
            re.IGNORECASE,
        ):
            return f"https://youtu.be/{matches.group(2)}"


if __name__ == "__main__":
    main()
