password = input("Enter your password: ")

min_length = 8

def check(password):

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False
    has_length = False
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

    if has_digit == True:
        score += 1
    if has_upper == True:
        score += 1
    if has_lower == True:
        score += 1
    if has_special == True:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Medium"
    elif score >= 5:
        strength = "Strong"

    
    result = {
        "score": score,
        "has_digit": has_digit,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_special": has_special,
        "has_length": has_length,
        "strength": strength
    }

    return result 

def display(results):

    print("Password Strength: " + results["strength"])
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

results = check(password)
display(results)