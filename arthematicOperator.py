def perform_operations(num1, num2):
    """Performs basic arithmetic operations and returns results."""
    results = {
        "Addition": num1 + num2,
        "Subtraction": num1 - num2,
        "Multiplication": num1 * num2,
        "Division": num1 / num2 if num2 != 0 else "Undefined (division by zero)",
        "Modulus": num1 % num2 if num2 != 0 else "Undefined (division by zero)",
        "Exponential": num1 ** num2,
    }
    return results

def main():
    try:
        num1, num2 = map(float, input("Enter two numbers separated by a comma: ").split(","))
        results = perform_operations(num1, num2)
        for operation, result in results.items():
            print(f"{operation}: {result}")
    except ValueError:
        print("Invalid input! Please enter two valid numbers separated by a comma.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
