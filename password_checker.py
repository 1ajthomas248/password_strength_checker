import math
import re
min_length = 8
common_passwords = ["123456", "admin", "12345678", "123456789", 
                    "password", "Pass@123", "admin123", "P@ssw0rd", "admin@123",
                    "Admin@123"]

def normalize_password_input(password):
    normalized = password.lower().strip()
    base = normalized

    base = re.sub(r"[!@#$%^&*]+$", "", base)
    base = re.sub(r"\d+$", "", base)
    base = re.sub(r"[!@#$%^&*]+$", "", base)
    return normalized, base 

def has_repeated_chars(password):
    if len(password) < 2:
        return False

    max_streak = 1
    current = 1

    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1

    return max_streak >= 4

def is_ascending(chunk):
    for i in range(1, len(chunk)):
        if ord(chunk[i]) != ord(chunk[i - 1]) + 1:
            return False
    
    return True

def is_descending(chunk):
    for i in range(1, len(chunk)):
        if ord(chunk[i]) != ord(chunk[i - 1]) - 1:
            return False
    
    return True

def has_sequence(password):
    p = password.lower()        

    for i in range (0, len(p) - 3):
        window = p[i:i+4]

        if not (window.isdigit() or window.isalpha()):
            continue

        if is_ascending(window) or is_descending(window):
            return True
        
    return False

    
def check(password):

    suggestions = []
    charset_size = 0
    entropy = 0

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False
    has_length = False
    is_common = False
    rule_score = 0
    strength = ""
    entropy_score = 0
    final_score = 0

    if len(password) >= min_length:
        has_length = True
        rule_score += 1
    if len(password) >= 12:
        rule_score += 1

    for i in password:
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
        if not i.isalnum():
            has_special = True
    
    repeat_chars = has_repeated_chars(password)
    sequence = has_sequence(password)
    
    for i in common_passwords:
        if i == password:
            is_common = True

    if has_digit == True:
        rule_score += 1
        charset_size += 10
    if has_upper == True:
        rule_score += 1
        charset_size += 26
    if has_lower == True:
        rule_score += 1
        charset_size += 26
    if has_special == True:
        rule_score += 1
        charset_size += 30
    
    if charset_size == 0:
        entropy = 0
    else: 
        entropy = len(password) * math.log2(charset_size)
    
    if entropy <= 28:
        entropy_score = 0
    elif entropy <= 40:
        entropy_score = 1
    elif entropy <= 60:
        entropy_score = 2
    elif entropy <= 80:
        entropy_score = 3
    else:
        entropy_score = 4

   
    final_score = rule_score + entropy_score

    if repeat_chars:
        final_score -= 2
        suggestions.append("Avoid long runs of the same character.")

    if sequence:
        final_score -= 1
        suggestions.append("Avoid predictable sequences like 1234 or abcd.")
    
    final_score = max(0, final_score)

    if final_score >= 9:
        strength = "Very Strong"
    elif final_score >= 7:
        strength = "Strong"
    elif final_score >= 5:
        strength = "Medium"
    elif final_score >= 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    
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
        "score": final_score,
        "entropy": entropy,
        "entropy_score": entropy_score,
        "is_common": is_common,
        "has_digit": has_digit,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_special": has_special,
        "has_length": has_length,
        "has_repeated_chars": repeat_chars,
        "has_sequence": sequence,
        "strength": strength,
        "suggestions": suggestions 
    }

    return result 

def display(results):

    if results['strength'] == 'Very Weak':
        print("Password Strength: " + '\033[1;31m' + results["strength"] + '\033[0m')
    elif results['strength'] == 'Weak':
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