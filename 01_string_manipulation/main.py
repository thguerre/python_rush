
# asks user input
numbers = []
numbers.append( input("Give me a number ! $ ") )
numbers.append( input("Give me yet another number ! $ ") )

# checks validity
for i in range(2):
    try:
        numbers[i] = int(numbers[i])
    except:
        print(f"\nOne of the entries ('{numbers[0]}' or '{numbers[1]}') isn't a number, process exiting !")
        exit()

# some number and string manipulation !
print("\nHere, i added both numbers together ! " + str(numbers[0] + numbers[1]))

# some unreadable triple nested parenthesis ternary syntax !
multiplied = numbers[0] * numbers[1]
print("\nThen, tried to multiply them too" + ((" : "+str(multiplied)) if multiplied != 0 else ".. and it gave a zero :("))
