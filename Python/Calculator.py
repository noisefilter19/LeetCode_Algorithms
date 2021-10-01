"""
Name : Maths Calculator
Author : [Mayank Goyal) [https://github.com/mayankgoyal-13]
"""

def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y
def divide(x, y):
    return x / y
def multiply(x, y):
    return x * y
def power(x, y):
    return x ** y

print("Select operation.")
print("A.Add")
print("B.Subtract")
print("C.Divide")
print("D.Multiply")
print("E.Power")

operator = input("Enter choice(A/B/C/D/E): ")

if operator in ('A', 'B', 'C', 'D', 'E'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operator == 'A':       
            print(num1, "+", num2, "=", add(num1, num2))
        elif operator == 'B':
            print(num1, "-" ,num2, "=", subtract(num1, num2))
        elif operator == 'C':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif operator == 'D':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif operator == 'E':
            print(num1, "**", num2, "=", power(num1, num2))

else:
     print("Invalid Input")
