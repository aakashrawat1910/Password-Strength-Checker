import re
import string

def check_password_strength(password):
    
    criteria_checks = []
    
    # Check minimum length
    if len(password) < 8:
        criteria_checks.append("Password must be at least 8 characters long")
    
    # Check for uppercase letters
    if not any(c.isupper() for c in password):
        criteria_checks.append("Password must contain at least one uppercase letter")
    
    # Check for lowercase letters
    if not any(c.islower() for c in password):
        criteria_checks.append("Password must contain at least one lowercase letter")
    
    # Check for digits
    if not any(c.isdigit() for c in password):
        criteria_checks.append("Password must contain at least one digit")
    
    # Check for special characters
    special_chars = set(string.punctuation)
    if not any(c in special_chars for c in password):
        criteria_checks.append("Password must contain at least one special character")
    
    # Password is strong if no criteria were failed
    is_strong = len(criteria_checks) == 0
    
    return is_strong, criteria_checks

def get_password_strength_feedback(password):
    
    is_strong, failed_criteria = check_password_strength(password)
    
    if is_strong:
        return "Strong password! All security criteria are met."
    else:
        feedback = "Password is not strong enough. Please address the following:\n"
        for criterion in failed_criteria:
            feedback += f"- {criterion}\n"
        return feedback

def main():
    
    print("Password Strength Checker")
    print("------------------------")
    print("Password must meet the following criteria:")
    print("- At least 8 characters long")
    print("- Contains both uppercase and lowercase letters")
    print("- Contains at least one digit (0-9)")
    print("- Contains at least one special character (!, @, #, $, %, etc.)")
    print("------------------------")
    
    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")
        
        if password.lower() == 'q':
            print("Exiting password checker.")
            break
            
        print("\nAnalyzing password strength...")
        feedback = get_password_strength_feedback(password)
        print(feedback)

if __name__ == "__main__":
    main()
