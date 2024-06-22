import random
import string


def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        print("Password length should be at least 4")
        return None

    ltrs  = string.ascii_letters
    dgts  = string.digits
    smbls = string.punctuation

    password = [
        random.choice(ltrs),
        random.choice(dgts),
        random.choice(smbls)
    ]

    all_chars = ltrs + dgts + smbls
    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)


def main():
    while True:
        try:
            length = int(input("Enter the length of the password You Want: "))
            password = generate_password(length)
            if password:
                print("Generated password:",password)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

        again = input("Do you want to generate another password? (yes/no): ")
        if again.lower() != 'yes':
            print("Exiting the password generator.")
            break


if __name__ == "__main__":
    main()
