import math
def exceptionHandle():

    def divide_by_zero():
        return 97/0

    def recurssion_error():
        return recurssion_error()

    def import_error():
        from math import abc

    def overflow_error():
        print(math.exp(1000))

    def index_error():
        l1 = []
        return l1[190]

    try:
        divide_by_zero()
    except ArithmeticError:
        print("1. Divide by Zero Error")

    try:
        recurssion_error()
    except RecursionError:
        print("2. Maximum recursion limit exceeded")

    try:
        import_error()
    except ImportError:
        print("3. Unable to import module")

    try:
        overflow_error()
    except OverflowError:
        print("4. Datatype size limit exceeded")

    try:
        index_error()
    except IndexError:
        print("5. List index out of range")

exceptionHandle()