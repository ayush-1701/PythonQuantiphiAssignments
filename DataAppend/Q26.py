name = input("Enter First Name:")
Lname = input("Enter Last Name:")
city = input("Enter City:")
age = int(input("Enter Age:"))

with open('myData.txt', 'r+') as f:
    f.seek(len(f.read()))

    f.write(f"\n{name}, {Lname}, {city}, {age}")
    #f.write("Aman, Agarwal, Mumbai, India\n")
    print("Data Append Successfully")
f.close()
