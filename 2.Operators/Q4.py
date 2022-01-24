# Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

rad = float(input("Enter the radius : "))

result = round((rad ** 2 * math.pi), 3)
print("Area of circle = ", result)
