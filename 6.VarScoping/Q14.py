def num_square(num):
    print(input_num)
    square = num * num
    return square


input_num = 11
if input_num > 100:
    result = num_square(5)
    print(result)


'''
Q1. What is the scope of num,square, input_num, result?
Ans: num -> num is a local variable. The scope is inside the function num_square
square -> square is a local variable. Whose scope is inside the function num_square
input_num -> input_num is a global variable. It can be used anywhere in the program
result -> num is also a variable. The scope of which is inside the condition 


Q2. What is the lifetime of each variable? When will they be created and destroyed?
Ans: 1 -> Local variables have a life from the start of the execution of 
the function to the end of execution, when the function ends, variable ends

2 -> Global variables live until the end of the application - 
until and unless the variable is explicitly deleted.


Q3. What would happen if input_num had a value of less than 100?
Ans: Nothing will be printed as the condition will fail, so it will be empty outpu.


Q4. What would be the scope and value of `result` if input_num has a value of less than 100?
Ans: result is a local variable. The scope of result is valid only inside function. 
And if the input_num value is less than 100 then the code will not output anything.
'''