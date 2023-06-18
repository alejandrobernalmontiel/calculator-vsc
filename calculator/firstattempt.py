def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2 
def divide(num1, num2):
    if num2 != 0:
            return num1 / num2
    else:
        return "error: can not divide by zero!"

print("welcome to the calculator")
num1 = float(input("enter the first number: "))
num2  = float(input("enter the second number: "))
print("-----result-----")
print("addition: ", add(num1, num2))
print("subtraction: ", subtract(num1, num2))
print("multiplication: ",multiply(num1, num2))
print("division: ", divide(num1, num2))