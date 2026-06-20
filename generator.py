import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Password Generator")
length = int(input("How long should the password be? "))
print("Generated Password:", generate_password(length))
