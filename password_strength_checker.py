import re

def is_length_valid(password):
    return len(password) >= 8

def has_uppercase(password):
    return re.search(r'[A-Z]', password) is not None

def has_lowercase(password):
    return re.search(r'[a-z]', password) is not None

def has_digit(password):
    return re.search(r'\d', password) is not None

def has_special_char(password):
    return re.search(r'[@$!%*?&]', password) is not None

def check_password_strength(password):
    strength = 0
    if is_length_valid(password):
        strength += 1
    if has_uppercase(password):
        strength += 1
    if has_lowercase(password):
        strength += 1
    if has_digit(password):
        strength += 1
    if has_special_char(password):
        strength += 1

    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

# Main Program
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
