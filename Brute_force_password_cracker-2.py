''' 
    Task 1) Brute Force Password Cracker  Python code
 
'''
#Importing Modules
import itertools #a module that provides various functions that work on iterators to produce complex iterators
import string    #a built-in type sequence
import time      #a module that provides various functions to work with time-related operations

#Function Definition: bruteforce_cracker
def bruteforce_cracker(password):
    '''  Takes a password as input.
    Generates all possible combinations of characters using itertools.product.
    Iterates through different lengths of guesses and combinations.
    Checks if the generated guess matches the provided password.
    If a match is found, returns the number of attempts, the correct guess, and the time taken.'''
    # Define the characters to be used in the guesses (printable characters)
    a = string.printable.strip()
    attempts = 0 # Counter for the number of attempts
    start_time = time.time()  # Record the starting time for measuring elapsed time

# Iterate through different lengths of guesses
    for length in range(1, len(password) + 1):
        # Generate all possible combinations of characters of the given length
        for guess in itertools.product(a, repeat=length):
            attempts += 1
            current_guess = ''.join(guess[:length])  # Extract the relevant part of the guess
            # Check if the current guess matches the provided password
            if current_guess == password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return (attempts, current_guess, elapsed_time)

    end_time = time.time()
    elapsed_time = end_time - start_time
    # Return a tuple containing the number of attempts, the correct guess (or None if not found), and the elapsed time
    return (attempts, None, elapsed_time)

def password_strength_checker(password):
    '''Function Definition: password_strength_checker
    Takes a password as input.
    Checks if the password meets certain criteria for strength:'''
    # Add your password strength criteria herein password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in string.punctuation for char in password)

    num_digits = sum(char.isdigit() for char in password)

    if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char and num_digits >= 2:
        return "Very Strong"
    elif len(password) >= 8 and has_uppercase and has_lowercase and has_digit:
        return "Strong"
    elif len(password) >= 6 and (has_uppercase or has_lowercase):
        return "Medium"
    else:
        return "Weak"

'''User Input:
Takes user input for the password to be cracked.'''

password = input("Input the password to crack: ")
strength = password_strength_checker(password)

print(f"Password strength: {strength}")
'''Password Strength Check:
    Calls password_strength_checker to evaluate the strength of the provided password.
    Prints the strength of the password.'''
attempts, guess, elapsed_time = bruteforce_cracker(password)
if strength == "Weak":
    print(f"Password cracked in {attempts} attempts and {elapsed_time:.2f} seconds.Password is too weak. Consider using a stronger password.The password is {guess}")
else:
    ''''Password Cracking Attempt:
        Calls bruteforce_cracker to attempt to crack the password.
        If the password is weak, it advises the user to use a stronger password.
        If the password is not weak, it prints the number of attempts, the correct guess (if found), and the time taken.'''
    if guess:
        print(f"Password cracked in {attempts} attempts and {elapsed_time:.2f} seconds. The password is {guess}.")
    else:
        print(f"Password not cracked after {attempts} attempts and {elapsed_time:.2f} seconds.")
