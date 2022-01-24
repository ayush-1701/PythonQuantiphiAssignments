# Create a function that checks if a number is a valid credit card number. If not it must return false otherwise true. The following are the conditions.
import re

card_no = (input("Enter Card Num: "))   #"4256-1101-4501-2626"
card = card_no.split("-")
new_card = ''.join(card)
group = list(set([len(i) for i in card]))

valid = False
if len(new_card) == 16 and len(re.findall("\d", new_card)) == 16 and group[0] == 4:
    if re.findall("\A3", card_no) or re.findall("\A4", card_no) or re.findall("\A9",card_no):
        valid = True

check = 0
if valid == True:
    for i in range(len(new_card) - 2):
        if new_card[i] == new_card[i + 1] and new_card[i + 1] == new_card[i + 2]:
            check += 1
            if check == 1:
                valid = False
                break

if valid == True:
    print("Credit Card is Valid")
else:
    print("Credit Card is not Valid")
