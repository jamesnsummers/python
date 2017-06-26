"""fizzbuzz function"""

#fizzbuzz dictionary
fizzbuzz_dict = {}
""" fizzbuzz dictionary function """
def fizzbuzz(max_num):
    """Loops through 1-max_num and prints message depending on evaluation of integer."""
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            fizzbuzz_dict['fizzbuzz'] = num
            print('FizzBuzz', num)
        elif num % 3 == 0:
            fizzbuzz_dict['fizz'] = num
            print('Fizz', num)
        elif num % 5 == 0:
            fizzbuzz_dict['buzz'] = num
            print('Buzz', num)
        else:
            fizzbuzz_dict['other'] = num
            print('Other', num)

fizzbuzz(20)
print(fizzbuzz_dict)
