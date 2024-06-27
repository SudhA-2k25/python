 # print all the Divisors (small no) of a number


def divis(n):

     for i in range(1,n+1):
         if n%i==0:
             print(i,end=" ")
        
    
obj = divis(6)


