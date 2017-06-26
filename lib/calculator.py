"""Calculator function using Python tutorial on digitalocean.com"""

# Define welcome() function to welcome the user
def welcome():
    """this is the function to welcome the user"""
    print('''
        Welcome to Calculator
        ''')
# Define calculate() function to ask calculate user entries
def calculate():
    """this is the function to calculate user entries"""
    operation = input('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ** for power
        % for modulo
        ''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()

# Define again() function to ask user if they want to use the calculator again
def again():
    """this is to see if user wants to calculate again"""
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

#Call welcome() outside of the function
welcome()
#Call calculate() outside of the function
calculate()
