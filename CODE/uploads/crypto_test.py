import hashlib

password = "admin123"

hash = hashlib.md5(password.encode())

print(hash.hexdigest())