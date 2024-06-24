def main():

    #created grocery list dict
    grocery_list = { }

    #populates dict and displays it per directions
    populate(grocery_list)


def populate(grocery_list):

    item = []

    while True:
        try:
            #adds items to "item" separated by "\n"
            item = input().upper()

        #looks for ctrl + d
        except EOFError:
            break

        else:
            if item in grocery_list:
                grocery_list[item] += 1

            else:
                grocery_list[item] = 1

            #print(grocery_list.values())

    # turns all dict. keys into a list
    glist = list(grocery_list)

    glist = sorted(glist)

    try:
        # prints out the key value followed by key itself
        for i in range(len(glist)):
            print(grocery_list[glist[i]], glist[i])

    except KeyError:
        pass

main()