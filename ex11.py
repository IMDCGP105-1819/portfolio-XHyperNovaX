from random import randint
x = randint(0, 100)
guess = x - 1
while guess != x:
    guess = int(input("Enter what you think the number is: "))
    if guess > x:
        print("Too high.")
    if guess < x:
        print("Too low.")
print("Correct, you got it!")
