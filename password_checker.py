password = input("Enter your password: ")

min_length = 8

def check(password):

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False
    has_length = False

    if len(password) >= min_length:
        has_length = True

    for i in password:
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
        if not i.isalnum():
            has_special = True

    if has_digit == False:
        print("Requirement not met: Lacking digit")
    if has_upper == False:
        print("Requirement not met: Lacking uppercase")
    if has_lower == False:
        print("Requirement not met: Lacking lowercase letter")
    if has_special == False:
        print("Requirement not met: Lacking special character")
    if has_length == False:
        print("Requirement not met: Character length too short")

check(password)