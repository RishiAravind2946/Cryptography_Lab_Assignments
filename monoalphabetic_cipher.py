def encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in plaintext.upper():
        if ch.isalpha():
            index = alphabet.index(ch)
            result += key[index]
        else:
            result += ch

    return result


def decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in ciphertext.upper():
        if ch.isalpha():
            index = key.index(ch)
            result += alphabet[index]
        else:
            result += ch

    return result


# Taking input from the user
key = input("Enter the 26-letter substitution key: ").upper()
plaintext = input("Enter the plaintext: ")

# Encryption
ciphertext = encrypt(plaintext, key)

# Decryption
decrypted = decrypt(ciphertext, key)

# Display output
print("\nPlaintext :", plaintext)
print("Encrypted :", ciphertext)
print("Decrypted :", decrypted)