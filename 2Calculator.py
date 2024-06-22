def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    """Main function to run the calculator."""
    while True:
        print("\nSimple Calculator (Console Version)")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == '1':
                    print("The result of addition is:", add(x, y))
                elif choice == '2':
                    print("The result of subtraction is:",subtract(x, y))
                elif choice == '3':
                    print("The result of multiplication is:", multiply(x, y))
                elif choice == '4':
                    result = divide(x, y)
                    print("The result of division is:", result)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
