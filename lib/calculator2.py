"""This is my calculator file that I learned how to do in class"""

def calculator(operation, numbers):
    """ takes an operation and perfomrms it on a list of numbers """
    results = 0

    if operation == "addition":
        for val in numbers:
            results += val

    if operation == "subtraction":
        index = 0
        for i in numbers:
            if index == 0:
                results = i
                index += 1
            else:
                results -= i

    if operation == "multiplication":
        results = 1
        for val in numbers:
            results *= val

    if operation == "division":
        index = 0
        for i in numbers:
            if index == 0:
                results = i
                index += 1
            else:
                results /= i
    return int(results)

NUMBERS = [24, 3, 4]
CALC_RESULT = calculator("division", NUMBERS)

print(CALC_RESULT)
