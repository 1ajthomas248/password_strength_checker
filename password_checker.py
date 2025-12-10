
min_length = 8
common_passwords = ["123456", "admin", "12345678", "123456789", 
                    "password", "Pass@123", "admin123", "P@ssw0rd", "admin@123",
                    "Admin@123"]

def check(password):

    suggestions = []

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
    
    if has_digit == False:
        suggestions.append("Add at least one number (0–9) to make the password harder to guess.")
    if has_upper == False:
        suggestions.append("Include at least one uppercase letter (A–Z) for better complexity.")
    if has_lower == False:
        suggestions.append("Include at least one lowercase letter (a–z) for better complexity.")
    if has_special == False:
        suggestions.append("Add at least one special character (e.g. !, @, #, $) for better complexity")
    if has_length == False:
        suggestions.append("Use at least 8 characters to meet the minimum length requirement.")
    if is_common == True:
        suggestions.append("Avoid common passwords; choose something more unique")
    if strength == "Very Strong":
        suggestions.append("This password is very strong. Good job!")

    result = {
        "score": score,
        "is_common": is_common,
        "has_digit": has_digit,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_special": has_special,
        "has_length": has_length,
        "strength": strength,
        "suggestions": suggestions 
    }

    return result 

def display(results):

    if results['strength'] == 'Weak':
        print("Password Strength: " + '\033[1;31m' + results["strength"] + '\033[0m')
    elif results['strength'] == 'Medium':
        print("Password Strength: " + '\033[1;33m' + results["strength"] + '\033[0m')
    elif results['strength'] == 'Strong':
        print("Password Strength: " + '\033[1;32m' + results["strength"] + '\033[0m')
    elif results['strength'] == 'Very Strong':
        print("Password Strength: " + '\033[1;36m' + results["strength"] + '\033[0m')

    print()

    if results["is_common"] == True:
        print('\033[1;31m' + "This password is known to be widely used and easily guessed. " \
        "Choose a different one." + '\033[0m')
    if results['has_digit'] == False:
        print("Requirement not met: " '\033[1;31m' +  "Lacking digit" + '\033[0m')
    if results['has_upper'] == False:
        print("Requirement not met: " '\033[1;31m' +  "Lacking uppercase letter" + '\033[0m')
    if results['has_lower'] == False:
        print("Requirement not met: " '\033[1;31m' +  "Lacking lowercase letter" + '\033[0m')
    if results['has_special'] == False:
        print("Requirement not met: " '\033[1;31m' +  "Lacking special character" + '\033[0m')
    if results['has_length'] == False:
        print("Requirement not met: " '\033[1;31m' +  "Password too short" + '\033[0m')
    
    print()

    print("Suggestions: ")
    for i in results['suggestions']:
        print("- " + i)

if __name__ == "__main__":
    print("-----------------------Password Strength Checker-----------------------")
    while True:
        password = input("Enter a password to analyze (or q to quit): ")
        if password == "quit" or password == "q":
            break
        elif password == "":
            print("Please enter a password or type q to quit")
        else:
            results = check(password)
            print()
            display(results)
            print("------------------------------------------------------------------------------------")