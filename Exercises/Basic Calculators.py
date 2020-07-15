def calculator1():
    num1 = int(input("Enter a number: ")) #the int turns it into an integer
    num2 = int(input("Enter another Number: ")) #python always assumes input is basic text rather than numbers
    #operation = input("Would you like to Add, Subtract, Multiply, or Divide?")
    num3 = float(input("Enter a decimal number: "))
    result = num1+num2+num3


    print(result)
calculator1()

def calculator2():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+,-,*,/ ): ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/' and num2 != 0:
        print(num1 / num2)
    else:
        print("Tried to destroy the world?")
calculator2()