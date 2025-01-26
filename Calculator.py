import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

print("Welcome to the basic calculator.")
def number_validation():
    """
    Prompts the user to choose a mathematical operation and provides validation for the operation and numbers.
    
    This function ensures the user inputs a valid operation number (1 to 4), and depending on the operation,
    it validates the input for numbers (either two numbers for subtraction/division or multiple numbers for addition/multiplication).
    
    It loops until valid inputs are provided.
    
    Return:
        tuple: A tuple containing the selected operation number (int) and a list of numbers (list of floats).
        The operation number corresponds to one of the following:
        - 1: Addition
        - 2: Subtraction
        - 3: Multiplication
        - 4: Division
    """
    try:    
        calculation_type = int(input("Choose an operation using the corresponding number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: "))
        if calculation_type not in [1,2,3,4]:
            print("Incorrect operation number. Try again.")
            number_validation()
    except ValueError:
        print("Oops! That wasn't a valid option.\nPlease make sure to enter numeric values from 1 to 4.")
        number_validation()

    if calculation_type in [2,4]:
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
        return (calculation_type, [number1, number2])
    
    elif calculation_type in [1,3]:
        numbers = input("Insert numbers to perform the operation on\nMake sure to separate the numbers with a comma: ")
        numbers_list = numbers.split(',')
        float_numbers_list = []
        for number in numbers_list:
            try:
                number = float(number)
                float_numbers_list.append(number)
            except ValueError:
                print("Incorrect value. Try again.")
                number_validation()
        return (calculation_type, float_numbers_list)
    

def calculator():
    """
    Performs the selected mathematical operation on a list of numbers input by the user.
    
    This function calls the `number_validation()` function to get the operation type and list of numbers.
    Based on the operation type, it performs the corresponding calculation (addition, subtraction, multiplication, or division).
    The result of the calculation is then printed.
    
    Return: 
    It prints the result of the calculation.
    """

    calculation_type, numbers = number_validation()
    result = None
    if calculation_type == 1:
        string_numbers = [str(number) for number in numbers]
        logging.info(f"I'm adding following numbers: {", ".join(string_numbers)}.")
        sum = 0
        for number in numbers:
            sum += number
        result = (f"The sum equals: {sum}.")
    elif calculation_type == 3:
        string_numbers = [str(number) for number in numbers]
        logging.info(f"I'm multiplying following numbers: {", ".join(string_numbers)}.")
        product = 1
        for number in numbers:
            product *= number
        result = print(f"The product equals: {product}")
    elif calculation_type == 2:
        logging.info(f"I'm subtracting {numbers[1]} from {numbers[0]}.")
        result = (f"The difference equals: {numbers[0] - numbers[1]}")
    elif calculation_type == 4:
        logging.info(f"I'm dividing {numbers[0]} by {numbers[1]}.")
        result = (f"The quotient equals: {numbers[0] / numbers[1]}.")
    if result is not None:
        print(result)

calculator()

    
    