num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "/":
    result = num1 / num2
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(f"{operation} is not a valid operation.")