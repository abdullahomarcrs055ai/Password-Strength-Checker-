def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    # Loop through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Check all conditions
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        print("Strong Password! ✅")
    else:
        print("Weak Password! ❌")
        print("Make sure your password has at least 8 characters, uppercase, lowercase, and numbers.")

# Main program
print("--- Simple Password Checker ---")
user_pass = input("Enter a password to check: ")
check_password(user_pass)
