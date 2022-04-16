import random

print ("Number Guessing Game")
num = random.randint(1, 9)

chance = 0
print("Guess a number (between 1 and 9) :")

while chance < 5:
    guess = int(input("Enter your guess :"))

    if guess == num:
        print ("Congratulations YOU WON !!")
        break

    elif guess < num:
        print ("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chance += 1

if not chance < 5:
    print ("You LOSE !! The number is", num)