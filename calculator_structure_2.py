from typing import Any


def calculator():

    result = Any

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter operator (+, -, *, /, %): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")

            else:
                result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            print("Invalid operator. Please try again.")

        print("Result:", int(result))

        another_calculation = input("Do you want to do another calculation? (yes/no): ")

        if another_calculation.lower() != 'yes':
            break


calculator()