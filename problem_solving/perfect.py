# Check a number is perfect or not
# perfect if sum of all its factors excluding the number itself is equal to the number
# 6 => 1,2,3,6 , 1+2+3 =6 so its a perfect number

def perfect(n):
    lst = [1]
    for i in range(2,n):
        if n%i==0:
            lst.append(i)

    if sum(lst) == n:
        print(n,"is a perfect number")
    else:
        print(n,"not a perfect number")

        


perfect(8)

        
