# Write a Python function which accepts two arguments x and y and returns (x + y) * (x + y).

def result(x, y):
    return pow((x + y), 2)
    #return (x+2)**2


num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

print("Result = ", result(num1, num2))
