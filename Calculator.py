import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

print("Welcome to the basic calculator.")
def number_validation():
    try:    
        calculation_type = int(input("Choose an operation using the corresponding number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: "))
        if calculation_type not in [1,2,3,4]:
            print("Incorrect operation number. Try again.")
            number_validation()
    except ValueError:
        print("Oops! That wasn't a valid option.\nPlease make sure to enter numeric values from 1 to 4.")
        number_validation()       
    try:
        number1 = float(input("Insert first number: "))
    except ValueError:
        print("Incorrect value. Try again.")
        number_validation()
    try:
        number2 = float(input("Insert second number: "))
    except ValueError:
        print("Incorrect value. Try again.")
        number_validation()
    return (calculation_type, number1, number2)

def calculator():
    calculation_type, number1, number2 = number_validation()
    
    result = None
    if calculation_type == 1:
        logging.info(f"I'm adding {number1} to {number2}.")
        result = (f"The result equals: {number1 + number2}.")
    elif calculation_type == 2:
        logging.info(f"I'm substracting {number2} from {number1}.")
        result = (f"The result equals: {number1 - number2}")
    elif calculation_type == 3:
        logging.info(f"I'm multiplying {number1} by {number2}.")
        result = (f"The result equals: {number1 * number2}")
    elif calculation_type == 4:
        logging.info(f"I'm dividing {number1} by {number2}.")
        result = (f"The result equals: {number1 / number2}.")
    print(result)

calculator()

    
    