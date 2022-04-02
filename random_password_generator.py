import secrets
import string
import os
import sys
import hashlib

MINIMUM_PASSWORD_LENGTH = 12

password_length = 0
special_chars = "!@#$'%^\"&*()[]{}-_"

while password_length < MINIMUM_PASSWORD_LENGTH:  # setting of the password minimum length
    print("Enter desired password length. \n~12 Characters minimum~")
    password_length = input()
    try:
        int(password_length)
    except ValueError:
        exit("Invalid input.")
    password_length = int(password_length)
    if password_length < MINIMUM_PASSWORD_LENGTH:
        print("Insufficient password length!\n")
source = string.ascii_letters + string.digits + special_chars
password = ''.join(secrets.choice(source) for i in range(password_length))

with open(os.path.join(sys.path[0], "common_passwords.txt"), "r") as pass_file:
    
#with open("common_passwords.txt") as pass_file:
    lines = pass_file.read().splitlines()
for line in lines:
    if line.rstrip() in password:  # checking password against known common passwords
        exit("Common password!")
print("Password:")
print(password)

encoded_password = password.encode('utf-8')  # password encoding
password_hash = hashlib.sha256(encoded_password).hexdigest()  # password hashing with SHA-256
print("Password hash:")
print(password_hash)
