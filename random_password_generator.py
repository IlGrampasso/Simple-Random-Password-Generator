import secrets
import string
import hashlib

passlen = 0
specialcharacters = "!@#$'%^\"&*()[]{}-_"

while passlen < 12:					#setting of the password minimum length
	print("Insert the password desired length.\n##Minimum 12 characters required##")
	passlen = int(input())
	if passlen < 12:
		print("Too short password!\n")
source = string.ascii_letters + string.digits + specialcharacters
password = ''.join(secrets.choice(source) for i in range(passlen))

f = open('pwds.txt', 'r')				#opening of the common password cheat sheet
lines = f.readlines()
for line in lines:
	if  line.rstrip() in password:			#checking if the password contains an easily guessable word of the cheat sheet
		exit("Password found in the cheat sheet")
print("Password:")
print(password)

encodedpwd = password.encode('utf-8')			#password encoding
hash = hashlib.sha256(encodedpwd).hexdigest()		#password hashing with SHA-256 algorithm
print("Password hash:")
print(hash)
