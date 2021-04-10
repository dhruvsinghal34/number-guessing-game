import random

name = input("Hello what is your name ")
number = random.randint (1,100)
print("Hi" + name + ", I am thinking of a number between to 1 and 100 ")
guessesTaken = 0

while guessesTaken < 5:
    guess = input("Enter a guess")
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print("That was too low.")
    elif guess > number:
        print("That was too high")
    else:
        break


if guess == number:
    print("Congratulation! you have won" + name + "you guessed the correct number")
else:
    print("You lose,too bad. Better luck next time.The right number was",number)
