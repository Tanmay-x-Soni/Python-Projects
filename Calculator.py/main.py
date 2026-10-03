from art import logo
        
def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    return num1 / num2

operations = {
    "+" : add , 
    "-" : subtract ,
    "*" : multiply , 
    "/" : divide
}

def calculator():
    calculate = 0
    program_running = True 

    print(logo)

    number1 = float(input("Enter the first number :  "))
    while program_running == True:
        
        operation = input(" + \n - \n * \n / \n Pick an operation :  ")
        number2= float(input("What's the next number : "))


        if operation == '+':
            calculate = operations["+"](num1=number1 , num2= number2)
        elif operation == '-':
            calculate = operations["-"](num1=number1 , num2= number2)
        elif operation == '*':
            calculate = operations["*"](num1=number1 , num2= number2)
        elif operation == '/':
            calculate = operations["/"](num1=number1 , num2= number2)
        else:
            print("Invalid operation , Try again!")
            break

        print(f"\n{number1} {operation} {number2} = {calculate}\n")
        number1 = calculate
        retry = input(f" Type 'y' to continue calculating with {number1} , or type 'n' to start a new calculation : ").lower()

        if retry == 'y':
            program_running== True
        elif retry == 'n':
            program_running== False
            print("\n" * 20)
            calculator()
        else:
            print("Invalid input! , Calculation stopped!")
            break

calculator()