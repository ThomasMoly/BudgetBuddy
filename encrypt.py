from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self, password, username, data):
        self.password = password.encode()
        self.username = username
        self.data = data

    def encrypt_write(self):
        cipher_suite = Fernet(self.password)
        cipher_text = cipher_suite.encrypt(self.data)
        with open(f"{self.username}.txt", "a") as file:
            file.write(cipher_text)
        return

    def decrypt_read(self):
        with open(f"{self.username}.txt", "a") as file:
            content = file.read()
        cipher_suite = Fernet(self.password)
        plain_text = cipher_suite.decrypt(content)
        return plain_text
    