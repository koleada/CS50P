def main():
    # prompt user for input
    word = input("Input: ")
    new = shorten(word)
    print(new)


def shorten(word):
    # cycle through each letter in user input
    for letter in word:

        # check if letter is upper case
        if letter.isupper():

            # f letter is upper case, check for an uppercase vowel
            if (
                letter == "A"
                or letter == "E"
                or letter == "I"
                or letter == "O"
                or letter == "U"
            ):
                # if vowel replace with nothing
                word = word.replace(letter, "")

        # check if letter is lowercase
        elif letter.islower():

            # if letter is lower, check for lowercase vowel
            if (
                letter == "a"
                or letter == "e"
                or letter == "i"
                or letter == "o"
                or letter == "u"
            ):

                # if vowel replace with nothing
                word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
