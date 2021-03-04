def calculate_apr(principal, interest_rate, years): #Takes in principle, interest_rate and years and calculates value of investment after X years'''
    if ((principle or interest_rate or years) <= 0):
        return False
    else: 
        total=float( (principle*(1+interest_rate)**years) )
        return total
