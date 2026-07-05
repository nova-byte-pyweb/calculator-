#nova_byte calculator project
# Simple Calculator Project 
options = {  
    1: "addition",
    2: "subtraction",
    3: "multiplication",
    4: "division",
    5: "floor division", 
    6: "modulus (remainder)", 
    7: "exponentiation",
    0: "Exit"
}

def calculate(x, y, user_choice):
    if user_choice == 1:
        return x + y
    elif user_choice == 2:
        return x - y
    elif user_choice == 3:
        return x * y
    elif user_choice == 4:
        if y == 0:
            return "Cannot divide by zero"
        return x / y
    elif user_choice == 5:
        if y == 0:
            return "Cannot divide by zero"
        return x // y
    elif user_choice == 6:
        if y == 0:
            return "Cannot divide by zero"
        return x % y
    elif user_choice == 7:
        return x ** y
    else:
        return "Invalid choice"

# LOOP START
while True:
    print("Calculator:")
    for key, value in options.items():
        print(f"{key}. {value}")

    user_choice = int(input("Choose operator: "))

    if user_choice == 0:
        print("Calculator stopped.")
        break

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = calculate(x, y, user_choice)
    print("Result:", result)