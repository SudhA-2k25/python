# GCD - Greatest Common Divisor
 #Divisor(small no) , Dividend(large no) , reminder
# reminder = dividend % divisor (general formula)

def gcd(a,b):
    if a>b:   # assuming reminder = 0
        dividend = a
        divisor = b  # small no
    else:
        dividend = b
        divisor = a

        #if rem != 0 spl.case
        
        rem = 1  # assume anything other than 0
        while rem!=0:
            rem = dividend%divisor
            
        if rem!=0:
            dividend = divisor
            divisor = rem

        return divisor

# calling the function
obj = gcd(3,2)
print(f"GCD = {obj}")
