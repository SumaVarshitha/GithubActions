import sys


def check_password(password):

    if len(password) < 8:
        return "Weak Password", "At least 8 characters needed"

    if password.islower():
        return "Weak Password", "Add uppercase letters"

    if password.isalpha():
        return "Weak Password", "Add numbers"

    return "Strong Password", "Good password"


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python password_checker.py <password>")
        sys.exit(1)

    password = sys.argv[1]

    status, suggestion = check_password(password)

    print("Status:", status)
    print("Suggestion:", suggestion)
