import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Şifre uzunluğunu girin: "))
password = generate_random_password(length)
print("Oluşturulan şifre:", password)
