user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = int(input("Enter your height in inches: "))
user_weight = int(input("Enter your weight in pounds: "))
user_eye_colour = input("Enter your eye colour: ")
user_hair_colour = input("Enter your hair colour: ")

if user_age > 0 and user_age < 12:
    print("You're a child.")
if user_age > 12 and user_age < 20:
    print("You're a teenager.")
if user_age > 20:
    print("You're an adult.")

if user_height > 69:
    print("You're taller than me.")
else:
    print("You're shorter than me.")

if user_weight > 130:
    print("You're heavier than me.")
else:
    print("You're lighter than me.")
