# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

def stringCheck(s):
    if len(s) < 2:
        return "Empty String"
    else:
        return s[:2] + s[len(s) - 2:]


S = input("Input a string : ")
res = stringCheck(S)
print(res)
