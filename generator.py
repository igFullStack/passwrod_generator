import random

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_multiple_passwords(num_passwords, length, chars):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, chars)
        passwords.append(password)
    return passwords

def get_user_input():
    num_passwords = int(input("Enter count of new passwords: "))
    password_length = int(input("Enter length of password: "))
    use_digits = input("Include (0123456789)? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include (abcdefghijklmnopqrstuvwxyz)? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include (!#$%&*+-=?@^_)? (yes/no): ").lower() == 'yes'
    exclude_ambiguous = input("Exclude (il1Lo0O)? (yes/no): ").lower() == 'yes'

    chars = ''
    if use_digits:
        chars += '0123456789'
    if use_uppercase:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lowercase:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if use_symbols:
        chars += '!#$%&*+-=?@^_'
    if exclude_ambiguous:
        ambiguous_chars = 'il1Lo0O'
        for char in ambiguous_chars:
            chars = chars.replace(char, '')

    return num_passwords, password_length, chars

def main():
    num_passwords, password_length, chars = get_user_input()
    passwords = generate_multiple_passwords(num_passwords, password_length, chars)

    print("\nNew Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
