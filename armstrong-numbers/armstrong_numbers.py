def is_armstrong_number(number):
    length = len(str(number))
    return sum(int(digit) ** length for digit in str(number)) == number
