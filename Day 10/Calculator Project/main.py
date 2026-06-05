def add(n1, n2):
    return n1 + n2

#TODO : Write out the other 3 functions that is subtract, divide and multiply
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

# TODO : Add these 4 functions to dictionary as the values . Keys = "+","-","/","*"

add_operation = add
sub_operation = subtract
div_operation = divide
mul_operation = multiply


calculator_functions ={
    "+":add,"-":subtract,"/":divide,"*":multiply
}