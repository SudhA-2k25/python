 # Palindrome Check for nos

def palindrome(n):
    s = str(n)

    if s==s[::-1]:
        print(n,"is a palindrome")
    else:
        print(n,"not a palindrome")

n = input("Enter : ")
palindrome(n)
