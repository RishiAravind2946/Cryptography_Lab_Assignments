
def rc4(data, key):
    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    result = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)

    return bytes(result)


plaintext = input("Enter plaintext: ")
key = input("Enter secret key: ")

encrypted = rc4(plaintext.encode(), key.encode())
print("Encrypted Text (Hex):", encrypted.hex().upper())

decrypted = rc4(encrypted, key.encode())
print("Decrypted Text:", decrypted.decode())
