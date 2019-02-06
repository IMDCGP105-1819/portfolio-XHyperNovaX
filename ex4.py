my_name = "Anthony Skipwith"
my_age = 18
my_height = 69
my_weight = 130
my_eyes = "Blue"
my_hair = "Black"
is_heavy = my_weight > 500

print(f"Let's talk about {my_name}.")
print(f"They are {my_height} inches tall.")
print(f"They are {my_weight} pounds heavy.")
#is_heavy works as a boolean statement from the result of if {my_weight} is greater than 500 pounds
print(f"It is {is_heavy} that they are overweight.")
print(f"They've got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}")

#=====

my_height_cm = round(my_height * 2.54, 1)
print(f"My height is {my_height} inches, which is also {my_height_cm} centimeters.")
my_weight_kg = round(my_weight * 0.45, 1)
print(f"My weight is {my_weight} pounds, which is also {my_weight_kg} kilograms.")
