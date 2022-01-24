# Write a function in a Python program to compute the greatest common divisor (GCD) of two positive integers.
def gcd(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf


n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"GCD of {n1} and {n2} =", gcd(n1, n2))
