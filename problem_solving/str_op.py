#Count the number of vowels in the string.
#Reverse the string.
#Convert the string to uppercase.
#Check if the string is a palindrome.

def string_operations(string_):
    vowels = 'aeiouAEIOU'
    # Count the number of vowels in the string
    vowel_count = sum(1 for char in string_ if char in vowels)
    
    # Reverse the string
    reversed_string = string_[::-1]
    
    # Convert the string to uppercase
    upper_case = string_.upper()
    
    # Check if the string is a palindrome
    is_palindrome = string_ == reversed_string
    
    return vowel_count, reversed_string, upper_case, is_palindrome

# Example usage:
result = string_operations("sudharshinee")

print("Number of vowels:", result[0])
print("Reversed string:", result[1])
print("Uppercase string:", result[2])
print("Is palindrome:", result[3])
