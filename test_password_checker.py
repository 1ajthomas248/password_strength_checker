from password_checker import check

# Flag Tests

def test_lowercase():
    result = check("abcdefg")
    assert result["has_lower"] is True
    assert result["has_digit"] is False
    assert result["has_upper"] is False
    assert result["has_special"] is False
    assert result["has_length"] is False
    assert result["strength"] == "Weak"

def test_uppercase():
    result = check("ABCDEFG")
    assert result["has_upper"] is True
    assert result["has_digit"] is False
    assert result["has_lower"] is False
    assert result["has_special"] is False
    assert result["has_length"] is False
    assert result["strength"] == "Weak"

def test_digit():
    result = check("1234567")
    assert result["has_digit"] is True
    assert result["has_lower"] is False
    assert result["has_upper"] is False
    assert result["has_special"] is False
    assert result["has_length"] is False
    assert result["strength"] == "Weak"

def test_special():
    result = check("!@#$%^&")
    assert result["has_special"] is True
    assert result["has_digit"] is False
    assert result["has_upper"] is False
    assert result["has_lower"] is False
    assert result["has_length"] is False
    assert result["strength"] == "Weak"

def test_length():
    result = check("11111111")
    assert result["has_length"] is True
    assert result["has_upper"] is False
    assert result["has_special"] is False
    assert result["has_lower"] is False
    assert result["strength"] == "Weak"

# Strength Tests

def test_medium_password():
    result = check("zYxW9876")
    assert result["strength"] == "Medium"
    

def test_strong_password():
    result = check("zYxW9876!")
    assert result["strength"] == "Strong"
    

def test_very_strong_password():
    result = check("zYxWv98765aBc123!")
    assert result["strength"] == "Very Strong"
    