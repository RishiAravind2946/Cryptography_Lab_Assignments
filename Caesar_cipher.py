
def encrypt(plaintext, shift):
    result = ""
    plaintext = plaintext.upper()

    for ch in plaintext:
        if ch.isalpha():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch

    return result


def decrypt(ciphertext, shift):
    result = ""
    ciphertext = ciphertext.upper()

    for ch in ciphertext:
        if ch.isalpha():
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += ch

    return result


plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(plaintext, shift)
decrypted = decrypt(encrypted, shift)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
