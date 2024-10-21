def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Math error: Division by zero"

def power(a, b):
    return a ** b

def calculator(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return power(num1, num2)
    else:
        return "Invalid operator"

while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /, ^): ")
        num2 = float(input("Enter the second number: "))

        result = calculator(num1, operator, num2)
        print("The result is:", result)

        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")	 	 	
