# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number : "))
if num % 2 == 0:
    print("Entered Number is an even number")
else:
    print("Entered Number is an odd number")