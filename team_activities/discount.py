from datetime import datetime

current_date_and_time = datetime.now(tz=None)

day_of_week = current_date_and_time.weekday()

# Variable for test the program in differents days to Tuesday and Wednesday
#day_of_week= 2

zero = False

while zero == False:
    subtotal = float(input("Please enter the subtotal: "))
    
    if day_of_week == 2 and subtotal <= 50 or day_of_week == 3 and subtotal <= 50:
        difference = 50 - subtotal
        print(f"You need only ${difference} more for obtain a discount in your purchase.")
    
    discount = 0
    if day_of_week == 2 and subtotal >= 50 or day_of_week == 3 and subtotal >= 50:
        discount = subtotal * 0.10
    
    subtotal -= discount
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amoun: {tax:.2f}")
    print(f"Total: {total:.2f}")
    
    if total == 0:
        zero = True