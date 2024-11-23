# Password-Strength-Checker

## Description
The Password Strength Checker is a Python-based utility designed to evaluate the strength of a password based on key security criteria. It ensures that passwords are robust and adhere to security best practices. Users can enter a password to receive feedback on its strength and suggestions for improvement.

## Features
- Validates passwords based on the following criteria:
  - Minimum length of 8 characters.
  - Contains at least one uppercase letter.
  - Contains at least one lowercase letter.
  - Includes at least one numeric digit (0-9).
  - Contains at least one special character (e.g., `!`, `@`, `#`, `$`, etc.).
- Provides detailed feedback on unmet criteria.
- User-friendly interface with an option to exit the program.
- Real-time password strength analysis.

## Prerequisites
- Basic understanding of Python.
- Python installed on your system (version 3.6 or later).

## Requirements
- Python 3.6 or later.
- No additional libraries are required (uses only Python's standard library).

## Using the Program
1. Clone or download the script file `password_strength_checker.py`.
2. Open a terminal or command prompt and navigate to the folder containing the script.
3. Run the script using the command:
   ```bash
   python password_strength_checker.py
   ```
4. Follow the on-screen instructions to enter passwords and evaluate their strength.

### Sample Inputs and Outputs

#### Input:
```plaintext
Enter a password to check (or 'q' to quit): Passw0rd!
```

#### Output:
```plaintext
Analyzing password strength...
Strong password! All security criteria are met.
```

---

#### Input:
```plaintext
Enter a password to check (or 'q' to quit): weakpass
```

#### Output:
```plaintext
Analyzing password strength...
Password is not strong enough. Please address the following:
- Password must contain at least one uppercase letter
- Password must contain at least one digit
- Password must contain at least one special character
```

---

#### Input:
```plaintext
Enter a password to check (or 'q' to quit): q
```

#### Output:
```plaintext
Exiting password checker.
```

## Notes
- This script does not store or log the entered passwords for security and privacy.
- Use this utility to evaluate password strength, not as a substitute for a password manager.

Feel free to contribute or suggest improvements!
