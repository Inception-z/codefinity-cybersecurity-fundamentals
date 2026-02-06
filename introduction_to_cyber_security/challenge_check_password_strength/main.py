import re

def check_password_strength(password):
    # Check if password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains at least one letter and one number
    if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
        return False
    
    return True

# Example usage:
password_to_check = "SecureP@ssw0rd"
if check_password_strength(password_to_check):
    print("Password is strong!")
else:
    print("Password does not meet the criteria.")