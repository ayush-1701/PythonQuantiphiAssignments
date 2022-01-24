# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

num = int(input("Input an number : "))
num1 = num
num2 = int(str(num)*2)
num3 = int(str(num)*3)
print("n+nn+nnn =", (num1+num2+num3))