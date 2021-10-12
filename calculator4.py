import linecache

MULTIPLY_SIGN = 'x'
ADD_SIGN = '+'
SUBTRACT_SIGN = '-'
DIVIDE_SIGN = '/'
QUIT = 'q'

FILE_NAME = 'step4.txt'
DELIMITATOR = ' '

CALCULATE_COMMAND = 'calc'
GOTO_COMMAND = 'goto'
REMOVE_COMMAND = 'remove'
REPLACE_COMMAND = 'replace'

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

    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    current_line = lines[0]
    current_line_number = 1
    line_numbers = [current_line_number]

    while True:
        try: 
            current_line = lines[current_line_number - 1]

            if (current_line[0] == REMOVE_COMMAND):
                del lines[current_line[1]]
            elif (current_line[0] == REPLACE_COMMAND):
                

        except IndexError:
            print('Index out of range')
            print('Line: ' + lines[line_numbers[-1] - 1])
            print('Line number: ' + str(line_numbers[-1]))
            break

    file.close()


main()
