from cryptography.fernet import Fernet


def encrypt_password():
    # Read encryption key from file
    with open('encryption_key.txt', 'rb') as file:
        key = file.read()

    # Create Fernet cipher suite
    cipher_suite = Fernet(key)

    # Read the last line from the file
    with open('password.txt', 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()  # Remove trailing newline

    # Encrypt the last line
    encrypted_last_line = cipher_suite.encrypt(last_line.encode())

    # Overwrite the file with all lines except the last one
    with open('password.txt', 'w') as file:
        file.writelines(lines[:-1])  # Write all lines except the last one

    # Append the encrypted last line to the file
    with open('password.txt', 'ab') as file:
        file.write(encrypted_last_line + b'\n')


# Call the function to encrypt the last line of the file
encrypt_password()
