# Q.1 Write a Python program to accept a string. Find and print the number of uppercase alphabets and lowercase alphabets.

# Function to count uppercase and lowercase letters
def count_case(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count

# Accepting the string from the user
input_string = input("Enter a string: ")

# Calling the function to count uppercase and lowercase letters
upper, lower = count_case(input_string)

# Printing the results
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")



Output:
Enter a string: Hello World
Uppercase letters: 2
Lowercase letters: 8