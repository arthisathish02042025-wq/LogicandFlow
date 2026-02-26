#Calculator Logic
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
Operator = input("Enter the operator(+,-,*,/):")

result = 0
if Operator == '+':
    result = num1 + num2
    print(f"Result = {result}")
elif Operator == '-':
    result = num1 - num2
    print(f"Result = {result}")
elif Operator == '*':
    result = num1 * num2
    print(f"Result = {result}")
elif Operator == '/':
    if num2 == 0:
      #Handle division by zero
      print("Error, Division by zero is not allowed.")
    else:
      result = num1 / num2
      print(f"Result = {result}")
else:
      #Handle invalid operator
      print("Error: Invalid operator entered. Please enter Operators +, -, *, /")

# check if result is positive, negative or zero and print accordingly
if result > 0:
   print("Positive")
elif result < 0:
   print("Negative")
else:
   print("zero")
