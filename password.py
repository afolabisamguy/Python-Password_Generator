from cryptography.fernet import Fernet
import string
import random


def encrypt_password():
    with open('encryption_key.txt', 'rb') as file:
        key = file.read()
    cipher_suite = Fernet(key)

    # Open the file in read mode
    with open('password.txt', 'r') as file:
        # Read all lines except the last one
        lines = file.readlines()
        last_line = lines[-1].strip()

    encrypted_last_line = cipher_suite.encrypt(last_line.encode())

    # Open the file in write mode
    with open('password.txt', 'w') as file:
        # Write the lines back to the file
        file.writelines(lines[:-1])

    with open('password.txt', 'ab') as file:
        file.write(encrypted_last_line + b'\n')


def decrypt_password():
    print('Welcome! You are trying to decrypt your password but first you need to verify your identity')
    print('Please enter your secret key')
    key = input()
    while key != '12345':
        print('Invalid key Please retry')
        key = input()
    else:
        with open('encryption_key.txt', 'rb') as file:
            key = file.read()

        cipher_suite = Fernet(key)
        encrypted = []

        with open('password.txt', 'rb') as file:
            for line in file:
                encrypted.append(line.strip())

        decrypted = []

        for enc in encrypted:
            try:
                decrypted_password = cipher_suite.decrypt(enc).decode()
                decrypted.append(decrypted_password + '\n')
            except Exception as e:
                print("Error decrypting password:", e)
                print("Encrypted:", enc)

        print("Decrypted Passwords:\n", *decrypted)


def password_generator():
    print('Welcome to sam\'s random password generator!')
    # TODO probably allow for choosing minimum of each character
    while True:
        print('Do you want to check your previously generated password? Enter Y')
        print('Enter N to generate a new password')
        answer = input()
        if answer == 'y':
            with open('password.txt', 'rb') as f:
                for record in f:
                    print(record)
            break
        elif answer == 'n':
            while True:
                try:
                    length = int(input('How long would you like your password to be? '))
                    while length < 5:
                        print('Password cannot be less than 5 characters... Please Try Again')
                        length = int(input('How long would you like your password to be? '))
                    break
                except ValueError:
                    print("Please enter a Valid Integer")
            print('Which Site Do You Want To Use The Password For?')
            site = input()
            print('Your password will automatically include upper case, lower case and digits')
            digits = string.digits
            uppercase = string.ascii_uppercase
            lowercase = string.ascii_lowercase
            spec_param = input('Would you like special characters in your password. Enter Y or N  ')
            if spec_param.lower() == 'y':
                lengths = length // 4
                remain = length % 4
                symbol = string.punctuation
                password = ''

                for _ in range(lengths):
                    dig = random.choice(digits) + random.choice(uppercase) + random.choice(lowercase) + random.choice(
                        symbol)
                    password += dig
            else:
                lengths = length // 3
                remain = length % 3
                password = ''

                for _ in range(lengths):
                    dig = random.choice(digits) + random.choice(uppercase) + random.choice(lowercase)
                    password += dig
            # print(length)

            if remain != 0:
                for _ in range(remain):
                    dig = random.choice(digits)
                    password += dig
            print(f'The Password for {site} is {password}')
            print("Do you want to save your password to a file? (Y/N)")
            save = input()
            if save == 'y':
                with open('password.txt', 'a') as password_file:
                    password_file.write(f'{site} - ')
                    password_file.write(password)
                    password_file.write('\n')
                encrypt_password()
            if save == 'n':
                print('Goodbye!')
            break
        else:
            print('Please enter (y/n)')


password_generator()
decrypt_password()

