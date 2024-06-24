# awesome lib that has tons of functions for validating user input (alternatively we could use https://pypi.org/project/validator-collection/)
import validators

input_email = input("What's your email address? ")

if validators.email(input_email) == True:
    print("Valid")
else:
    print("Invalid")
