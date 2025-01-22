"""
If the car’s speed is greater than 45 miles per hour, the driver gets the ticket
"""
"""
if car_speed is greater than 45
then print ticket
"""
"""
if boolean_expression:
    statements
"""
car_speed = float(input("Enter the speed: "))
if (car_speed > 45 and car_speed <= 55):
    print("You get a warning")
elif car_speed > 55:
    print("You get a ticket")
else:
    print("Good driver")
