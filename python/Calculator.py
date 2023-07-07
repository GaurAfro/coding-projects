# Simple calculator program

while True: # This starts an infinite loop
    # Print a Menu to the User
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit program")
    
    # Take Input from the User
    choice = int(input("Enter choice(1/2/3/4/5): "))
    
    # Check if user wants to exit the program
    if choice == 5:
        print("Exiting the program")
        break # this will break the loop and end the program
    
    # Check if choice is valid
    if 1 <= choice <= 4: # If the input is in the correct range
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
    # Perform the Operations
    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)
    
    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)
    
    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)
    
    elif choice == 4:
        if num2 != 0: # To avoid division by zero
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Devision by zero is not allowe.")
    
    else:
        print("Invalid input! Please try again. ")