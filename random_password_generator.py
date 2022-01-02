import secrets
import string
import hashlib

MINIMUM_PASSWORD_LENGTH = 12

passlen = 0
specialcharacters = "!@#$'%^\"&*()[]{}-_"

while passlen < MINIMUM_PASSWORD_LENGTH:					#setting of the password minimum length
    print("Insert the password desired length.\n##Minimum 12 characters required##")
    passlen = input()
    try:
        int(passlen)
    except:
        exit("You have not inserted a number, try another time!")
    passlen = int(passlen)
    if passlen < MINIMUM_PASSWORD_LENGTH:
        print("Too short password!\n")
source = string.ascii_letters + string.digits + specialcharacters
password = ''.join(secrets.choice(source) for i in range(passlen))

with open("pwds.txt", "r") as f:				#opening of the common password cheat sheet
    lines = f.read().splitlines()
for line in lines:
    if  line.rstrip() in password:			#checking if the password contains an easily guessable word of the cheat sheet
        exit("Password found in the cheat sheet")
print("Password:")
print(password)

encodedpwd = password.encode('utf-8')			#password encoding
hash = hashlib.sha256(encodedpwd).hexdigest()		#password hashing with SHA-256 algorithm
print("Password hash:")
print(hash)
