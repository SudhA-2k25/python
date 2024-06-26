# count digits in a number

n = int(input("Enter any number : "))

result = sum(int(digit) for digit in str(n) )
print(result)
