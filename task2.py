def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for numbers and operation
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter operation (1/2/3/4): ")

    # Perform calculation
    if choice == '1':
        result = num1 + num2
        op = '+'
    elif choice == '2':
        result = num1 - num2
        op = '-'
    elif choice == '3':
        result = num1 * num2
        op = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("Invalid operation choice.")
        return

    # Display result
    print(f"\nResult: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()
