# Rail Fence Cipher
# Encryption and Decryption

def encrypt(plaintext, rails):
    if rails == 1:
        return plaintext

    rail_text = [""] * rails
    row = 0
    direction = 1

    for ch in plaintext:
        rail_text[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(rail_text)


def decrypt(ciphertext, rails):
    if rails == 1:
        return ciphertext

    length = len(ciphertext)

    # Find the rail number for each character
    pattern = []
    row = 0
    direction = 1

    for _ in range(length):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Count characters in each rail
    counts = [0] * rails

    for r in pattern:
        counts[r] += 1

    # Divide ciphertext into rails
    rail_data = []
    index = 0

    for count in counts:
        rail_data.append(list(ciphertext[index:index + count]))
        index += count

    # Reconstruct plaintext
    positions = [0] * rails
    plaintext = ""

    for r in pattern:
        plaintext += rail_data[r][positions[r]]
        positions[r] += 1

    return plaintext


# Main program
plaintext = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

if rails <= 0:
    print("Invalid number of rails!")
elif rails > len(plaintext) and len(plaintext) > 0:
    print("Number of rails cannot be greater than message length.")
else:
    encrypted = encrypt(plaintext, rails)
    decrypted = decrypt(encrypted, rails)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)