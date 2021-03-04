def calculator(number1, number2, operator): #performs operations on user input
    if operator == '+':
        return float(number1 + number2)  
    elif operator == '-':
        return float(number1 - number2)
    elif operator == '*':
        return float(number1 * number2)
    elif operator == '/':
        return float(number1 / number2)
    elif operator == '//':
        return float(number1 // number2)
    elif operator == '**':
        return float(number1 ** number2)
    else:
        return False

def input_output(): #asks user for input and calls calculator function to perform operations and asks if they want to exit or continue
    while True :
        print ('Enter first number: ')
        number1=input()
        number1=float(number1)
        print ('Enter second number: ')
        number2=input()
        number2=float(number2)
        print ('Enter operation: ')
        operator=input()
        
        print(calculator(number1, number2, operator))
        print('Do you wish to exit?')
        user=input()
        if user== 'n' :
            continue
        else:
            break

