import uuid
from cryptography.fernet import Fernet



class PasswordManager:
    def __init__(self, machine_id, master_password):
        self.machine_id = machine_id
        self.master_password = master_password
        self.records1 = {}
        self.records2 = {}
        self.authentication = Authentication()

    def authenticate(self, password):
        return self.master_password == password

    def set_master_password(self, new_password):
        self.master_password = new_password
        return True

    def test_reset_master_password(self):
        self.master_password = ""
        return True

    def add_record(self, record):
        self.records1[record.title] = record
        self.records2[record.username] = record
        return True

    def search_record_by_title(self, title):
        return self.records1.get(title, None)

    def search_record_by_username(self, username):
        return self.records2.get(username, None)

    def delete_record(self, record):
        del self.records1[record.title]
        del self.records2[record.username]
        return True


class Authentication:
    def authenticate_with_uuid3(self, namespace, name):
        uuid3 = uuid.uuid3(namespace, name)
        return self.authenticate(str(uuid3))
    
class Encrypt:
    def encrypt(self, text):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())
        return encrypted_text
    
class Decrypt:
    def decrypt(self, text):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(text.encode())
        return decrypted_text.decode()
        return text

