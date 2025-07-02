import re

def check(pw):
    errors = []
    if len(pw) < 12: errors.append("Too short")
    if not re.search(r'[A-Z]', pw): errors.append("Missing uppercase")
    if not re.search(r'[a-z]', pw): errors.append("Missing lowercase")
    if not re.search(r'[0-9]', pw): errors.append("Missing number")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', pw): errors.append("Missing special char")
    if "password" in pw.lower(): errors.append("Contains 'password'")
    return errors or ["Strong password"]
