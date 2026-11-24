# Password Strength Checker 🛡️

A Python command-line security tool that evaluates password strength based on core cybersecurity rules and provides actionable feedback to make weak passwords stronger.

## Features
- Checks password length (minimum 8 characters).
- Verifies the presence of uppercase letters, lowercase letters, digits, and special characters using Python's `re` module.
- Calculates a strength score out of 5 (`Weak`, `Moderate`, or `Strong`).
- Displays specific tips for missing security criteria.

## How to Run
1. Ensure Python is installed on your system.
2. Run the script in your terminal:
   ```bash
   python password_checker.py
   ```
3. Enter any password to analyze its security level.
