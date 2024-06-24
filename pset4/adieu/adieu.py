def getNames():
    names = []  
    while True: 
        
        # get names and add each to the list
        try:
            newnName = input("Name: ")
            names.append(newnName)
        
        # on ctrl+D return the list 
        except EOFError:
            return names 
        
nameList = getNames() 

# start of the print statement, using end to remove the default new line 
print("Adieu, adieu, to ", end="")

if (len(nameList) > 2):
    for name in nameList:
        # check if its the last name, if not just add a comma 
        if (name != nameList[len(nameList)-1]): 
            print(name, end=", ")
        # if last name then print this way 
        else:
            print("and " + name)

 # 2 names entered 
elif (len(nameList) == 2):
    print(nameList[0] + " and " + nameList[1])

# 1 name entered  
else:
    print(nameList[0])