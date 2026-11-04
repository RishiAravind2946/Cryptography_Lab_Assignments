
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt(plaintext, key):
    key = key.ljust(16)[:16].encode()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext.hex().upper()


def decrypt(ciphertext, key):
    key = key.ljust(16)[:16].encode()

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(bytes.fromhex(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()

    return plaintext.decode()


plaintext = input("Enter plaintext: ")
key = input("Enter secret key: ")

encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
