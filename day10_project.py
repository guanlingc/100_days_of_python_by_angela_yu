import resource.calculator_art as art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculator_functions ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
""" Main body of script"""

def calculator():
    print(art.logo)
    retain_result = True
    f_num = float(input("What's the first number? "))
    while retain_result:
        for function in calculator_functions:
            print(function)
        operation = input('Pick an operation form above ')
        next_num = float(input("What's the next number? "))

        result = calculator_functions[operation](f_num, next_num)
        print(f'{f_num} {operation} {next_num} = {result}')
        reuse_calculator = input('do you want to continue using this result? type "y" or "n" ')
        if reuse_calculator == 'y':
            f_num = result
        else:
            retain_result = False
            print(f'The final result is {result}')
            calculator() # this is for recursion 

calculator()