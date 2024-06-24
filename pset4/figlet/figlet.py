import sys 
from pyfiglet import Figlet 
#exception raised when an invalid font is used
from pyfiglet import FontNotFound

if (len(sys.argv) > 1):
    
    if(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        print("Invalid Usage")
        sys.exit(1) 
    else:
        font = sys.argv[2]
        try:
            f = Figlet(font=font)
        except FontNotFound:
            print("Invalid usage")
            sys.exit(1)
        else:
            userText = input("Input: ")
            print(f.renderText(userText))
else:
    f = Figlet()
    userText = input("Input: ")
    print(f.renderText(userText))