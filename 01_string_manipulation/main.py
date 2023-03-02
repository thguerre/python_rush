
# asks user input
firstNumber = input("Give me a number ! $ ")
secondNumber = input("Give me yet another number ! $ ")

# checks validity
if (not firstNumber.isnumeric() or not secondNumber.isnumeric()):
    print(f"\nOne of the entries ('{firstNumber}' or '{secondNumber}') isn't a number, process exiting !")
    exit()

# parse integers
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

# some number and string manipulation !
print("\nHere, i added both numbers together ! " + str(firstNumber + secondNumber))

# some unreadable triple nested parenthesis ternary syntax !
multiplied = firstNumber * secondNumber
print("\nThen, tried to multiply them" + ((" "+str(multiplied)) if multiplied != 0 else ".. and it gave a zero :("))
