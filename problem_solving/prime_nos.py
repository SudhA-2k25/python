

# Print prime nos

def prime_nos(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")

prime_nos(13)

# check its a prime no

def check_prime(n):
    if n <= 1:
        print(n, "is not a prime number")
        return

    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            return

    print(n, "is a prime number")

# Example usage:
check_prime(13)  # Output: 13 is a prime number
check_prime(4)   # Output: 4 is not a prime number

