from password_checker import check_password


def test_weak_password():
    assert check_password("abc") == "Weak Password"


def test_missing_number():
    assert check_password("HelloWorld") == "Add numbers"


def test_strong_password():
    assert check_password("Hello123") == "Strong Password"