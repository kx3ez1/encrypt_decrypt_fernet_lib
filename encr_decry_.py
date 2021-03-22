def encrypt_data(data):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    print(key)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decrypt_data(key, data):
    from cryptography.fernet import Fernet,InvalidToken
    fernet1 = Fernet(key)
    try:
        return fernet1.decrypt(data).decode()
    except InvalidToken:
        return None
