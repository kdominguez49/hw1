def calculate_apr(principal, interest_rate, years): #Takes in principle, interest_rate and years and calculates value of investment after X years'''
    print('Enter principle: ')
    principle=input()
    print('Enter interest_rate: ')
    interest_rate=input()
    interest_rate=float(interest_rate)
    print('Enter years: ')
    years=input()

    if ((principle or interest_rate or years) <= 0):
        print('FALSE')
    else 
        total=float( (principle*(1+interest_rate)**years) )
        print (total)
