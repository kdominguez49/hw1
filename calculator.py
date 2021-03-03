def calculator(number1, number2, operator): #performs operations on user input
    if operator == '+':
        print (operator1 + operator2)   
    elif operator == '-':
        print (operator1-operator2)
    elif operator == '*':
        print (operator1*operator2)
    elif operator == '/':
        print (operator1/operator2)
    elif operator == '//':
        print (operator1//operator2)
    elif operator == '**':
        print (operator1**operator2)
    elif operator != '+' or '-' or '*' or '/' or '//' or '**':
        return false

def input_output(input): #asks user for input and calls calculator function to perform operations and asks if they want to exit or continue
    while operation!= false :
        print ('Enter first number: ')
        number1=input()
        number1=float(number1)
        print ('Enter second number: ')
        number2=input()
        number2=float(number2)
        print ('Enter operation: ')
        operator=input()
        calculator(number1, number2, operation)
        print('Do you wish to exit?')
        if input== 'n' :
            continue
        else:
            break

