# Check for Amstrong Number
# An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself
# 371 => if 3^3 + 7^3 + 1^3 =371 , then its an amstrong number , 153

def ams(n):

    string = str(n)
    sum = ( (int(string[0])**3) + (int(string[1])**3) + (int(string[2])**3) )

    if n==sum:
        print(n,"Amstrong Number!")
    else:
        print(n,"not an amstrong number")

n = int(input("enter your number : "))
ams(n)

