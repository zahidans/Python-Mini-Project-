import random
import string

pass_len =  9

charValue = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValue)

print(f"your password is {password}")