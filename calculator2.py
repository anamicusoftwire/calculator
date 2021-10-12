
MULTIPLY_SIGN = 'x'
ADD_SIGN = '+'
SUBTRACT_SIGN = '-'
DIVIDE_SIGN = '/'
QUIT = 'q'
FILE_NAME = 'step2.txt'
DELIMITATOR = ' '
CALCULATE_COMMAND = 'calc'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return float(a) / b

def multiply(a, b):
    return a * b

def calculate(operation, a, b):
    if operation == MULTIPLY_SIGN:
        return multiply(a, b)
    if operation == ADD_SIGN:
        return add(a, b)
    if operation == DIVIDE_SIGN:
        return divide(a, b)
    if operation == SUBTRACT_SIGN:
        return subtract(a, b)

    print('Error: Undefined operation\n')
    return None

def main():
    file = open(FILE_NAME, 'r')
    sum = 0

    for line in file:
        [command, operation, a, b] = line.split(DELIMITATOR)
        a = int(a)
        b = int(b)

        if command == CALCULATE_COMMAND:
            sum = sum + calculate(operation, a, b)

    print('Result: ' + str(sum))
    
    file.close()


main()
