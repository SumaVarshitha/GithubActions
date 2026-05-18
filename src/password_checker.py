def check_password(password):

    if len(password) < 8:
        return "Weak Password", "Password should contain at least 8 characters"

    if password.islower():
        return "Weak Password", "Add uppercase letters"

    if password.isalpha():
        return "Weak Password", "Add numbers"

    return "Strong Password", "Good password"


if __name__ == "__main__":

    user_password = input("Enter password: ")

    status, suggestion = check_password(user_password)

    print("Status:", status)
    print("Suggestion:", suggestion)
