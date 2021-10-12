import linecache

MULTIPLY_SIGN = 'x'
ADD_SIGN = '+'
SUBTRACT_SIGN = '-'
DIVIDE_SIGN = '/'
QUIT = 'q'
FILE_NAME = 'step3.txt'
DELIMITATOR = ' '
CALCULATE_COMMAND = 'calc'
GOTO_COMMAND = 'goto'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

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

def get_line_number_for_goto_command(line):
    command = line.split(DELIMITATOR)
    
    if command[0] != GOTO_COMMAND:
        return

    line_number = None

    if command[1] == CALCULATE_COMMAND:
        operation = command[2]
        a = int(command[3])
        b = int(command[4])
        line_number = calculate(operation, a, b)
    else:
        line_number = int(command[1])

    return line_number

def main():
    file = open(FILE_NAME, 'r')
    current_line = linecache.getline(FILE_NAME, 1)
    current_line_number = 1
    line_numbers = [current_line_number]

    while True:
        next_line_number = get_line_number_for_goto_command(current_line)

        if (next_line_number in line_numbers):
            print('Line: ' + current_line)
            print('Line number: ' + str(current_line_number))
            break
        
        line_numbers.append(next_line_number)
        current_line_number = next_line_number
        current_line = linecache.getline(FILE_NAME, next_line_number)

    file.close()


main()
