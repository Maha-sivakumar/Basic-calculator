def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

print("Basic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("The addition of {0} and {1} is {2}".format(num1,num2,result))
elif choice == '2':
    result = subtract(num1, num2)
    print("The subtraction of {0} and {1} is {2}".format(num1,num2,result))
elif choice == '3':
    result = multiply(num1, num2)
    print("The multiplication of {0} and {1} is {2}".format(num1,num2,result))
elif choice == '4':
    result = divide(num1, num2)
    print("The division of {0} and {1} is {2}".format(num1,num2,result))
else:
    print("Invalid input. Please select a number between 1 and 4.")
