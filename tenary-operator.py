# Three examples of tenary operators

# Example #1
distance_travel = input("Enter the distance to travel in kilometers: ")
take_aireplane = True if int(distance_travel) > 300 else False
print(f"Should I take the airplane? {take_aireplane}")


# Example #2
number = input("Please enter a number: ")
print(number,"is positive") if int(number) > 0 else print(number,"is negative")


# Example #3
shoot_distance = input("Enter the distance of the basketball shot: ")
print("Your basket is a 2 point shot") if float(shoot_distance) < 23.9 else print("Your basket is a 3 point shot")

