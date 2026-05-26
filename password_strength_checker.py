print("========== Password Stength Checker ==========")

# password = "avneeshYdv@12"  --> This is strong password !!

import string
while True:
    password = input("Enter password: ")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_spacial = any(c in string.punctuation for c in password)
    long_enough = len(password) >= 8

    if has_upper and has_lower and has_digit and has_spacial and long_enough:
        print("Password strength STRONG!!")
        break
    else:
        print("Password strength WEAK!!")