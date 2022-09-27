import secrets
import string
print('hello, Welcome to Password generator!')
length = int(input('\nEnter the length of password: '))
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))  # for a 20-character password
print(password)