from cryptography.fernet import Fernet

# Read the key from the file
with open('encryption_key.txt', 'rb') as file:
    key = file.read()

cipher_suite = Fernet(key)

# Read encrypted passwords from the file
encrypted_passwords = []

with open('password.txt', 'rb') as file:
    for line in file:
        encrypted_passwords.append(line.strip())

# Decrypt passwords
decrypted_passwords = []

for encrypted_password in encrypted_passwords:
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    decrypted_passwords.append(decrypted_password)

print("Decrypted passwords:", decrypted_passwords)
