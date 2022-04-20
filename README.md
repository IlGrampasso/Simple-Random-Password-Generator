# Simple-Random-Password-Generator
This simple Python script generates a password by selecting a random sequence of characters, choosing from numbers, normal and special characters.
The randomness of the combination is reached trough the usage of "secrets" module.
The length of the password is asked to the user (minimum 12 charecters). The user has also the possibility to copy it directly to the clipoboard selecting "y".
Eventually, the script assures that the output password does not include any of the common words from the cheatsheet (common_passwords.txt). 