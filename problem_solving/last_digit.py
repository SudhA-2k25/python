# 2 numbers, the base a and the index b.find the last digit of a^b.

# 1) Find the pattern for each number
# 2 --> 4,8,6,2 , like that

# take last digit of a(34) means take 4 , and if b%4==0 take b as 4 else take b%4 value
# here 4 is the pattern length
#now a^b%4 and if 2 digits answer came means do a modulus %10

def last_digit(a, b):
    # Step 1: Handle special cases
    if b == 0:
        return 1  # Any number to the power of 0 is 1
    if a == 0:
        return 0  # 0 to any power is 0
    
    # Step 2: Find the last digit of the base
    last_digit_base = a % 10
    
    # Step 3: Identify the repeating pattern of the last digits
    pattern = []
    current = last_digit_base
    while current not in pattern:
        pattern.append(current)
        current = (current * last_digit_base) % 10
    
    # Step 4: Determine the effective exponent
    pattern_length = len(pattern)
    effective_exponent = b % pattern_length
    if effective_exponent == 0:
        effective_exponent = pattern_length
    
    # Step 5: Compute the last digit of a^b using the pattern
    return pattern[effective_exponent - 1]

# Example usage
a = 34
b = 10
print(last_digit(a, b))  # Output: 4
