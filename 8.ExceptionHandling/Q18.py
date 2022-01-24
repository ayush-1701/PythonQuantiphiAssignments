arr = []
result = []
class MyError(Exception):

    def __init__(self, age, name, email, phn):
        self.age = age
        self.name = name
        self.email = email
        self.phn = phn

    def check_name(self):  # if length of name is greater than or equal to 3 then name is valid
        try:
            if len(self.name) >= 3:
                arr.append(self.name)
            else:
                raise MyError('', "Exception InvalidNameError: Name length must be greater than 3", '', '')
        except MyError as error:
            print(error.name)

    def check_ages(self):  # if age is greater than 0 then age is valid
        try:
            if self.age > 0:
                arr.append(self.age)
            else:
                raise MyError("Exception AgeInvalidError: Age must be greater than 0", '', '', '')
        except MyError as error:
            print(error.age)

    def check_email(self):  # if email contains '@' and '.' then email is valid
        try:
            if '.' in self.email and '@' in self.email:
                arr.append(self.email)
            else:
                raise MyError('', '', "Exception InvalidEmailError: Email must contains @ and .", '')
        except MyError as error:
            print(error.email)

    def check_phn(self):  # if length of phone number is 10 then phone number is valid
        try:
            if len(self.phn) == 10:
                arr.append(self.phn)
            else:
                raise MyError('', '', '', "Exception InvalidPhoneNumberError: Phone number should be 10 digits")
        except MyError as error:
            print(error.phn)


ob = MyError(10, "AyushKR", "ayuK117gmailcom", "935972354446")  # Given input
ob.check_ages()
ob.check_name()
ob.check_email()
ob.check_phn()

#correct perosn
ob1 = MyError(10, "AyushKR", "ayuK117@gmail.com", "9359723546")  # Given input
ob1.check_ages()
ob1.check_name()
ob1.check_email()
ob1.check_phn()
if len(arr) == 4:
    print(arr)
else:
    arr.clear()
