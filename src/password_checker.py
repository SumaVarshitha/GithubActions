def check_password(password):
    if len(password) < 8:
        return "Weak Password"

    if password.islower():
        return "Add uppercase letters"

    if password.isalpha():
        return "Add numbers"

    return "Strong Password"


if __name__ == "__main__":
    user_password = input("Enter password: ")

    result = check_password(user_password)

    print(result)
