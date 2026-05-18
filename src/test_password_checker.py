from password_checker import check_password


def test_weak_password():
    status, suggestion = check_password("abc")
    assert status == "Weak Password"


def test_missing_uppercase():
    status, suggestion = check_password("hello123world")
    assert status == "Weak Password"


def test_strong_password():
    status, suggestion = check_password("Hello123")
    assert status == "Strong Password"
