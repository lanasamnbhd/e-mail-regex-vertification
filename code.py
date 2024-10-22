import re

def emailVert(email):
    email_regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex,email):
        return True
    else:
        return False

email=input("enter your email address: ")

if emailVert(email):
    print("valid email")
else:
    print("invalid email")
