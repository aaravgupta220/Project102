#Manual Task - People get bored so they spend money on buying video games or pay to watch tv
#Solution - Rather than paying (a very lenghty process) I invented a free game that is pretty addicting
#This game saves a lot of time - now rather than wasting money and scrolling for hours to find something to watch
#I can simply play this game

import random

print("Guess my age")

number = random.randint(1,70)

chances = 0

if number <= 15 :
    print("Guess my age! (Hint : I'm still a minor.)")
elif number > 15 & number < 59 :
    print("Guess my age! (Hint : I'm an adult)")
else : 
    print("Guess my age! (Hint : I'm old)")

while chances < 5 : 

    guess=int(input("Enter your guess :- "))

    if guess == number:
        print("Congratulations you won")
        break

    elif guess < number :
        print("Your guess was too low: My age is higher than that", guess)

    else :
        print("Your guess was too high: My age is lower than that", guess)

    chances += 1

if not chances < 5 :
    print("You lose, my age is", number)