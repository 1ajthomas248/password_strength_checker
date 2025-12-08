min_length = 8
common_passwords = ["123456", "admin", "12345678", "123456789", 
                    "password", "Pass@123", "admin123", "P@ssw0rd", "admin@123",
                    "Admin@123"]

def check(password):

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False
    has_length = False
    is_common = False
    score = 0
    strength = ""

    if len(password) >= min_length:
        has_length = True
        score += 1
    if len(password) >= 12:
        score += 1

    for i in password:
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
        if not i.isalnum():
            has_special = True
    
    for i in common_passwords:
        if i == password:
            is_common = True

    if has_digit == True:
        score += 1
    if has_upper == True:
        score += 1
    if has_lower == True:
        score += 1
    if has_special == True:
        score += 1

    if score == 6 and len(password) > 14:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif 3 <= score <= 4:
        strength = "Medium"
    elif score <= 2:
        strength = "Weak"
    
    if is_common == True:
        strength = "Weak"

    result = {
        "score": score,
        "is_common": is_common,
        "has_digit": has_digit,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_special": has_special,
        "has_length": has_length,
        "strength": strength,
    }

    return result 

def display(results):

    print("Password Strength: " + results["strength"])
    if results["is_common"] == True:
        print("This password is known to be widely used and easily guessed. " \
        "Choose a different one.")
    if results['has_digit'] == False:
        print("Requirement not met: Lacking digit")
    if results['has_upper'] == False:
        print("Requirement not met: Lacking uppercase letter")
    if results['has_lower'] == False:
        print("Requirement not met: Lacking lowercase letter")
    if results['has_special'] == False:
        print("Requirement not met: Lacking special character")
    if results['has_length'] == False:
        print("Requirement not met: Password too short")    

while True:
    password = input("Enter your password: ")
    if password == "quit" or password == "q":
        break
    elif password == "":
        print("Please enter a password or type q to quit")
    else:
        results = check(password)
        display(results)