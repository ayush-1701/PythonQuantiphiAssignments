import math
import mathFunc

sinFun = int(input("Enter an Angle: "))
print(f"sin({sinFun}) = ", math.sin(sinFun))

num1 = int(input("Enter Length: "))
num2 = int(input("Enter Width: "))
flight = int(input("Flight Num: "))

print(mathFunc.area(num1, num2))
print("Population of City is: ", mathFunc.Population)
print(mathFunc.flights(flight))
