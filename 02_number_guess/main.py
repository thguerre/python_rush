
# imports
from random import randrange, randint


# rules
print("The rule of this game is quite simple:")
print("- I choose a random \"maximum\", 100, 1 000 or 10 000")
print("- Then i chose yet another random number between 0 and the first one")
print("- You'll give it a try, and find the solution following my hints !")
print("\n Do your best to find the solution with the smallest amount of attempts :)")


# set variables and start game loop
rangeMax = 10 ** randint(2, 4)
solution = randint(0, rangeMax)
attempts = 1


print("\nThe number you have to guess if between 0 and " + str(rangeMax) + " (inclusive)")
print("[DEV] Solution : " + str(solution))

while True:
    guess = input(f"\nGuess !\n ({attempts}) > ")
    try:
        guess = int(guess)
    except:
        print("Invalid input")
        continue
    if guess == solution:
        break
    print("Higher !" if guess < solution else "Lower !")
    attempts += 1

print(f"Solved in {attempts} attempts !")

