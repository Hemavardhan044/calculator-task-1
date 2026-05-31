def calculator():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Calculator Closed!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid Choice! Try Again.")
            continue

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            result = num1 + num2
            operation = "+"

        elif choice == "2":
            result = num1 - num2
            operation = "-"

        elif choice == "3":
            result = num1 * num2
            operation = "*"

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = "/"

        print(f"{num1} {operation} {num2} = {result}")


calculator()
