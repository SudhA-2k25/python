# number = 34 , reverse = 43
# output shd be :-  number ^ reverse % (10^9 + 7)
# Given a number and its reverse. Find that number raised to the power of its own reverse.


import math 
num = int(input("enter number : "))
rev = int( str(num)[::-1] )
print(rev)

modd =  10**9 +7 

result= pow(num , rev , modd)
print(result)

# pow(base, exp, mod%)
