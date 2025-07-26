password = input("Enter a password: ")

length_ok = len(password) >= 8
digit_ok = False
lower_ok = False
upper_ok = False
special_ok = False

special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

for char in password:
    if char.isdigit():
        digit_ok = True
    
    elif char.islower():
        lower_ok = True

    elif char.isupper():
        upper_ok = True

    
    elif char in special_chars:
        special_ok = True

if length_ok and digit_ok and lower_ok and upper_ok and special_ok:
    print(" Strong password!")

else:
    print("Weak password! Please include:")
    if not length_ok:
        print("- At least 8 characters")
    if not digit_ok:
        print("- At least one digit")
    if not lower_ok:
        print("- At least one lowercase letter")
    if not upper_ok:
        print("- At least one uppercase letter")
    if not special_ok:
        print("- At least one special character (e.g. !, @, #)")
