# Double Columnar Transposition
# Encryption and Decryption


def get_order(key):
    """
    Returns column indices in alphabetical order of the key.
    """
    return sorted(range(len(key)),
                  key=lambda i: (key[i].upper(), i))


def columnar_encrypt(text, key):
    """
    Performs one columnar transposition encryption.
    """
    columns = len(key)
    order = get_order(key)

    encrypted = ""

    for col in order:
        encrypted += text[col::columns]

    return encrypted


def columnar_decrypt(ciphertext, key):
    """
    Performs one columnar transposition decryption.
    """
    columns = len(key)
    length = len(ciphertext)

    # Number of rows
    rows = (length + columns - 1) // columns

    # Number of characters in each column
    column_lengths = []

    for col in range(columns):
        column_lengths.append(
            (length - col + columns - 1) // columns
        )

    # Store characters for each column
    column_data = [""] * columns

    order = get_order(key)

    index = 0

    for col in order:
        count = column_lengths[col]
        column_data[col] = ciphertext[index:index + count]
        index += count

    # Read row by row
    plaintext = ""

    for row in range(rows):
        for col in range(columns):
            if row < len(column_data[col]):
                plaintext += column_data[col][row]

    return plaintext


def double_encrypt(plaintext, key1, key2):
    """
    Applies columnar transposition twice.
    """
    intermediate = columnar_encrypt(plaintext, key1)
    ciphertext = columnar_encrypt(intermediate, key2)

    return ciphertext


def double_decrypt(ciphertext, key1, key2):
    """
    Reverses the second transposition first,
    then reverses the first transposition.
    """
    intermediate = columnar_decrypt(ciphertext, key2)
    plaintext = columnar_decrypt(intermediate, key1)

    return plaintext


# Main program
plaintext = input("Enter plaintext: ")
key1 = input("Enter first key: ").strip()
key2 = input("Enter second key: ").strip()

if len(key1) == 0 or len(key2) == 0:
    print("Invalid key!")
else:
    encrypted = double_encrypt(plaintext, key1, key2)
    decrypted = double_decrypt(encrypted, key1, key2)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)