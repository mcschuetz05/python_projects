
def addition(number1, number2):
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")


def subtraction(number1, number2):
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")


def multiplication(number1, number2):
    result = number1 * number2
    print(f"{number1} x {number2} = {result}")


def division(number1, number2):
    if number2 == 0:
        print("Division by zero is not allowed!")
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")


operations = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division
}


def main():
    calculating = True
    while calculating:

        print("\nSimple Calculator")
        print("\nSelect operation:"
              "\n1. Addition"
              "\n2. Subtraction"
              "\n3. Multiplication"
              "\n4. Division")

        try:
            choice = int(input("\nEnter choice (1-4): "))
        except ValueError:
            print("Please enter a valid input.")
            continue

        if choice not in operations:
            print("Invalid choice.")
            continue

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice in operations:
            operations[choice](number1, number2)
        else:
            print("Invalid choice.")

        if not input("Do you want to perform another calculation? (yes/no): ").lower().strip().startswith("y"):
            print("Okay, byeeee!")
            return


main()
