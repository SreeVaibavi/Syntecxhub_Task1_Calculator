def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero")
        return None
    return x / y


print("Simple Calculator")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", subtract(num1, num2))
elif op == "*":
    print("Result:", multiply(num1, num2))
elif op == "/":
    result = divide(num1, num2)
    if result is not None:
        print("Result:", result)
else:
    print("Invalid operator")
