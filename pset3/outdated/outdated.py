def main(): 
    
    # dict of months for easy conversion to number format
    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    
    # this function is responsible for prompting the user for a date and verifying the input string
    def getDate():
        while True:
            userDate = input("Date: ").strip()
            
            if (userDate[0].isalpha()):
                # split into a list (month, day, year) if first char is a letter
                userDate = userDate.split()
                try:
                    # get the number representation of the month
                    userDate[0] = months[userDate[0]]
                except KeyError:
                    pass
                
                else:
                    # check for a , after the day
                    if (userDate[1].find(",") == -1):
                        pass
                    # remove comma and check the int day to see if its above 31 
                    elif (int(userDate[1].replace(",", "")) > 31):
                        pass
                    else:
                        # actually remove the comma this time and return the value 
                        userDate[1] = userDate[1].replace(",", "")
                        return userDate
            elif (userDate[1] == "/" or userDate[2] == "/"):
                userDate = userDate.split("/")
                
                # check for bad formatting or incorrect dates
                if (userDate[1].isalpha() or int(userDate[0]) > 12 or int(userDate[1]) > 31):
                    pass
                
                else:
                    return userDate
            else: 
                    pass
            
        
    userDate = getDate()
    month = userDate[0]
    day = userDate[1]
    year = userDate[2]
    
    if (type(day) == str):
        day = int(day.replace(",", ""))
    
    # add padded  if necessary 
    if (int(day) < 10):
        day = "0"+ str(day)
        
    # add padded  if necessary
    if (int(month) < 10):
        month = "0" + str(month)
    
    print(f"{year}-{month}-{day}")
        
    
        
main()