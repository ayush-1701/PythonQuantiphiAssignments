# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

str1 = input("Enter the string : ")

if str1[:2] == 'Is' or str1[:2] == 'is':
    print("Result : ", str1)
else:
    print("Result : ", ('Is' + str1))
