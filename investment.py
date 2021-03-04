def calculate_apr(principal, interest_rate, years): #Takes in principle, interest_rate and years and calculates value of investment after X years'''
    if ( (principal<=0) or (interest_rate<=0) or (years<= 0) ):
        return False
    else: 
        total=float( (principal*(1+interest_rate)**years) )
        return total
