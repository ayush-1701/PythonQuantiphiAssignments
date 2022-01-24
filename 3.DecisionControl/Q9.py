# Write a Python program to test whether a passed letter is a vowel or not.

str1 = input("Enter a character : ")

vowels = ['A', 'E', 'I', 'O', 'U']

if str1.upper() in vowels:
    print(str1, "is a Vowel")
else:
    print(str1, "is a Consonant")
