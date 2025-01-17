import random
# find out more about random.randint on https://www.w3schools.com/python/module_random.asp

print("The computer has chosen a number between 1 and 50, can you guess it?")
print("The computer will tell you if your guess is higher, lower, or correct.")

# ==> TASK: FIX THIS NEXT LINE SO THAT A RANDOM NUMBER BETWEEN 1 & 50 IS PICKED
num = random.randint(10, 50) #Picks a random number between the numbers in the brackets

guess = int(input("What is your guess? "))
while True:
    # ==> TASK: FIX THIS SELECTION SO THAT YOU CAN GUESS THE CORRECT NUMBER & QUIT THE LOOP!
    if guess > num:
        print("The number is lower than that, guess again.")
    elif guess < num: 
        print("The number is higher than that, guess again.")
    guess = int(input("What is your guess? "))

print("Congrats! You guessed the computer's number")