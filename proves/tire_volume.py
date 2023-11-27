from datetime import datetime
import math

current_day = datetime.now(tz=None)

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input(" Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")

if width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 560
    print(f"The price of your tires is {price}")
elif width == 225 and aspect_ratio == 55 and diameter == 17:
    price = 940
    print(f"The price of your tires is {price}")
elif width == 195 and aspect_ratio == 50 and diameter == 16:
    price = 842
    print(f"The price of your tires is {price}")
elif width == 215 and aspect_ratio == 65 and diameter == 18:
    price = 928
    print(f"The price of your tires is ${price}")


buy = input("Do you want to buy tires? (yes/no): ").lower()

if buy == "yes":
    phone = input("What's your phone number? ")
else:
    phone = None
    
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_day:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}", file=volumes_file)