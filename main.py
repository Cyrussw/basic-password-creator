import random
import os
import hashlib

os.system("cls")

# Variables

lower = "abcdefghifklmnopqrstuvwxyz"
upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."
result = lower + upper + numbers + symbols
length = int(input("Şifre Uzunluğunu Girin: "))

password = "".join(random.sample(result,length))

# Result

print("Created Password:", password)
print("MD5:", hashlib.md5(password.encode('utf-8')).hexdigest())
