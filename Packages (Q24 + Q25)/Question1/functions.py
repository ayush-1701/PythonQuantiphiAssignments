from pack import addition, subtraction, div, multiply

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

res1 = addition(num1, num2)
res2 = subtraction(num1, num2)
res3 = div(num1, num2)
res4 = multiply(num1, num2)

print(res1, "\n", res2, "\n", res3, "\n", res4)
