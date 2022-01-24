# Write a Python program to concatenate all elements in a list into a string and return it.

str1 = ''
list1 = [1, 10, 8, 'q', 5, 'T', 'A', 17]

for i in list1:
    str1 += str(i)

print("Elements of List in string: ", str1)
