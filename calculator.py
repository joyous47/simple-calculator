# --- Simple Calculator Program ---

def calculate():
    """
    Asks the user for two numbers and a mathematical operation,
    then performs the operation and prints the result.
    Handles basic error cases like invalid input or division by zero.
    """
    print("Welcome to the Simple Python Calculator!")

    # 1. Get the first number from the user
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num1 = float(num1_str) # Convert input to a floating-point number
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 2. Get the second number from the user
    while True:
        try:
            num2_str = input("Enter the second number: ")
            num2 = float(num2_str) # Convert input to a floating-point number
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 3. Get the mathematical operation from the user
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break # Exit loop if operation is valid
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    # 4. Perform the operation based on user input
    result = None # Initialize result variable
    expression = f"{num1_str} {operation} {num2_str}" # String for printing

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return # Exit function if division by zero
        else:
            result = num1 / num2
    else:
        # This else block should ideally not be reached due to the while loop above
        print("An unexpected error occurred with the operation.")
        return

    # 5. Print the result
    print(f"{expression} = {result}")

# Call the calculate function to run the program
if __name__ == "__main__":
    calculate()
