
MULTIPLY_SIGN = 'x'
ADD_SIGN = '+'
SUBTRACT_SIGN = '-'
DIVIDE_SIGN = '/'
MOD_SIGN = '%'
POWER_SIGN = '^'
QUIT = 'q'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return float(a) / b

def multiply(a, b):
    return a * b

def modulo(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculate(operation, a, b):
    if operation == MULTIPLY_SIGN:
        return multiply(a, b)
    if operation == ADD_SIGN:
        return add(a, b)
    if operation == DIVIDE_SIGN:
        return divide(a, b)
    if operation == SUBTRACT_SIGN:
        return subtract(a, b)
    if operation == MOD_SIGN:
        return modulo(a, b)
    if operation == POWER_SIGN:
        return power(a, b)

    print('Error: Undefined operation\n')
    return None

def main():
    while True:
        operation = input('Enter operation:\n')

        if (operation == QUIT):
            break

        a = int(input('First number:\n'))
        b = int(input('Second number:\n'))
        result = calculate(operation, a, b)

        if result:
            print('Result: ' + str(result))

main()
