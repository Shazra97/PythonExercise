print("Welcome to my smart Calculator")

num1= int(input("Enter first number"))
num2=int(input("Enter 2nd number"))
opr=input("Enter operator +,-,*,/,% ")

match opr:
    case '+':
        print("Addition", num1+num2)
    case '-':
        print("Subtraction", num1-num2)
    case '*':
        print("Multiply", num1*num2)
    case '/':
        print("Division", num1/num2)
    case '%':
        print("Modulus", num1%num2)
    case _:
        print("Operator invalid, Try again")

        print("Thank you for using smart Calculator")