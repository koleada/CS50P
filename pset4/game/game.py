import random


def main():

    def getNum():
        while True:
            try:
                n = int(input("Level: "))
            except ValueError:
                pass
            else:
                if n > 0:
                    return n
                else:
                    pass

    userNum = getNum()
    compNum = random.randint(1, userNum)

    #    print(f"compNum = {compNum}")

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                pass
        except ValueError:
            pass
        else:
            if guess < 1:
                pass
            else:
                if guess > compNum:
                    print("Too large!")
                    pass
                elif guess < compNum:
                    print("Too small!")
                    pass
                else:
                    print("Just right!")
                    break


main()
