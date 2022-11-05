import secrets
import string
import os
import sys
import hashlib
import pyperclip as pc

MINIMUM_PASSWORD_LENGTH = 6 # setting of the password minimum length

error_flag = 0 #flag for error detection on the input
password_length = 0
special_chars = "!@#$'%^\"&*()[]{}-_" 

while int(password_length) < MINIMUM_PASSWORD_LENGTH:
    print("Enter the desired password length. \n~6 characters minimum (but 12 characters is recommended)~")
    password_length = input()
    try: #checking the value is an integer
        int(password_length)
    except ValueError: 
        print("Invalid input!")
        password_length = 0
        error_flag = 1
    if error_flag == 1:
        error_flag = 0
        continue # starting a new cycle
        
    if int(password_length) < MINIMUM_PASSWORD_LENGTH: #checking password length
        print("Insufficient password length!\n")

print("Do you want to copy the password to the clipboard? [y/n] (Default is n)")
choice = input()

password_length = int(password_length)
if password_length < MINIMUM_PASSWORD_LENGTH:
    print("Insufficient password length!\n")

source = string.ascii_letters + string.digits + special_chars # password generation
password = ''.join(secrets.choice(source) for i in range(password_length))

with open(os.path.join(sys.path[0], "common_passwords.txt"), "r") as pass_file: # opening the known common password file 
    lines = pass_file.read().splitlines()
for line in lines:
    if line.rstrip() in password:  # checking password against known common passwords
        exit("Common password!")
print("Password:")
print(password)
if choice=="y":
    pc.copy(password)

encoded_password = password.encode('utf-8')  # password encoding
password_hash = hashlib.sha256(encoded_password).hexdigest()  # password hashing with SHA-256
print("Password hash:")
print(password_hash)
