import re

inp_date = 'June 01 1965'
char = inp_date.split(" ")

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

if char[0].lower() in months and re.findall("[0-3][0-9]", char[1]) and len(re.findall("\d", char[2])) == 4:
    if int(char[1]) <= 31 and (months.index(char[0].lower()) + 1) != 2:
        print("Date is Valid")

    elif (months.index(char[0].lower()) + 1) == 2:
        if int(char[2]) % 4 == 0 and int(char[1]) <= 29:
            print("Date is Valid")
        elif int(char[2]) % 4 != 0 and int(char[1]) <= 28:
            print("Date is Valid")
        else:
            print("Date is not Valid")

    elif (months.index(char[0].lower()) + 1) % 2 == 0 and (months.index(char[0].lower()) + 1) != 2:
        if int(char[1]) <= 30:
            print("Date is Valid")
        else:
            print("Date is not Valid")

    else:
        print("Date is not valid")

else:
    print("Date is not valid")
