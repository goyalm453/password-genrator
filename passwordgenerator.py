import random
import string

# Prompt the user for the length of the password
length = int(input("Enter the length of the password: "))

# Prompt the user for the type of characters to include in the password
char_type = input("Enter the type of characters to include (letters, digits, special, or all): ")

# Generate a random password
if char_type == "letters":
    password = ''.join(random.choices(string.ascii_letters, k=length))
elif char_type == "digits":
    password = ''.join(random.choices(string.digits, k=length))
elif char_type == "special":
    password = ''.join(random.choices(string.punctuation, k=length))
else:
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Print the password
print(password)
