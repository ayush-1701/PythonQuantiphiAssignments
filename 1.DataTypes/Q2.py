#2] Write a Python program to get the largest number from a list.

l1 = [12, 15, 9, 64, 53, 66, 19, 81, 76, 55, 44, 90, 5, 83]

maxVal = 0
for i in l1:
    if maxVal < i:
        maxVal = i
print("Maximum Number =", maxVal)

# Method 3
l1.sort()
print("Maximum Number (using BuiltIn func) = ",l1[len(l1) - 1])
