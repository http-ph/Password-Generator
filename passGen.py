import random

def passwordGenerator():

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    especials = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    stringToGen = "abcdefghijklmnopqrstuvwxyz"

    print("\n############################################")
    print("\nWelcome, let's start our password generator")
    print("\n############################################\n")

    passwordLenght = input("Characters lenght:\n\n")
    if ( passwordLenght.isdigit() != True):
        return print("Your password lenght is not a number.")
    else:
        passwordLenght = int(passwordLenght)

    if ( passwordLenght < 5 ):
        return print("Your password lenght must be more than 5 characters.")
    elif passwordLenght > 20 :
        return print("Your password lenght must be less than 20 characters.")


    passwordCaseSens = input("\nYour password would have uppercase letters?\n\n")
    if (passwordCaseSens == "y"):
        stringToGen += upper

    passwordNumb = input("\nYour password would have numbers?\n\n")
    if passwordNumb == "y":
        stringToGen += numbers

    passwordEspChac = input("\nYour password must include especial characters?\n\n")
    if passwordEspChac == "y":
        stringToGen += especials


    output_string = ''.join(random.SystemRandom().choice(stringToGen) for _ in range(passwordLenght))

    print("\n#############################\n")
    print("YOUR PASSWORD HAS BEEN GENERATED\n")
    print('You password is: ' + output_string)
    print("\n###############################")

if __name__ == "__main__":
    passwordGenerator()