# Python-Password_Generator

## Project Description
This is a Python-based project that generates, encrypts, and decrypts passwords. The user can generate strong random passwords, save them to a file, encrypt them for security, and decrypt them later by verifying their identity. This project uses the `cryptography` library to handle encryption and decryption securely.

### Features:
- **Random Password Generation**: The user can generate strong passwords of a desired length, including uppercase, lowercase, digits, and optional special characters.
- **Password Encryption**: After generating a password, the user has the option to save it to a file, which is then encrypted for security.
- **Password Decryption**: The user can decrypt and view the previously saved passwords by providing the correct secret key.
- **Multiple Site Support**: Passwords can be generated for different websites and stored along with the site's name.

## Project Structure

```
.
├── decryption.py             # Handles password decryption
├── encrypted_password.txt    # Contains the encrypted password(s)
├── encryption.py             # Handles password encryption
├── encryption_key.txt        # Contains the encryption key
├── password.py               # The main script for password generation, encryption, and decryption
├── password.txt              # Stores plaintext and encrypted passwords
```

### `password.py`
This script:
- Prompts the user to generate a password or view previously generated passwords.
- Saves the generated passwords to a text file.
- Encrypts the saved password using the `Fernet` symmetric encryption method.
- Provides a decryption option to view the encrypted passwords after verifying the user's identity.

### `encryption.py`
This file contains the encryption logic used to securely store passwords in `password.txt`.

### `decryption.py`
This script handles decryption by asking the user for a secret key, verifying it, and then decrypting the saved passwords.

### `password.txt`
Stores both plaintext and encrypted passwords. Plaintext passwords are automatically encrypted when they are saved to the file.

### `encrypted_password.txt`
Stores encrypted passwords securely.

### `encryption_key.txt`
Stores the key used for encryption and decryption.

## How to Run

1. **Install Dependencies**:
   - Make sure you have Python installed.
   - Install the required libraries using:
     ```
     pip install cryptography
     ```

2. **Run the Script**:
   - Execute the `password.py` file to start generating passwords:
     ```
     python password.py
     ```

3. **Generating Passwords**:
   - Choose whether to generate a new password or view previously saved passwords.
   - Generated passwords can be saved to a file and encrypted.

4. **Decrypting Passwords**:
   - Run the `decrypt_password()` function to view the stored encrypted passwords after verifying the secret key.

## Requirements
- Python 3.x
- `cryptography` library

## License
This project is licensed under the MIT License.
