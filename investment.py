def calculate_apr(principal, interest_rate, years): #Takes in principle, interest_rate and years and calculates value of investment after X years'''
    if ((principal or interest_rate or years) <= 0):
        return False
    else: 
        total=float( (principal*(1+interest_rate)**years) )
        return total
