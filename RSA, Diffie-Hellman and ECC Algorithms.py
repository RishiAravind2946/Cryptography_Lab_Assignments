from math import gcd


# ---------------- RSA ALGORITHM ----------------

def rsa():
    print("\n--- RSA ALGORITHM ---")

    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    message = int(input("Enter message: "))

    if p <= 1 or q <= 1 or p == q:
        print("Invalid prime numbers.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    if message < 0 or message >= n:
        print("Message must be between 0 and n-1.")
        return

    # Select the public exponent
    e = 65537

    if e >= phi or gcd(e, phi) != 1:
        e = 3
        while e < phi and gcd(e, phi) != 1:
            e += 2

    if e >= phi:
        print("Unable to select a suitable public exponent.")
        return

    # Calculate the private exponent
    d = pow(e, -1, phi)

    # Encryption and decryption
    ciphertext = pow(message, e, n)
    decrypted = pow(ciphertext, d, n)

    print("\nRSA Results")
    print("Modulus (n):", n)
    print("Totient (phi):", phi)
    print("Public Exponent (e):", e)
    print("Private Exponent (d):", d)
    print("Public Key:", (e, n))
    print("Private Key:", (d, n))
    print("Original Message:", message)
    print("Encrypted Message:", ciphertext)
    print("Decrypted Message:", decrypted)


# ------------- DIFFIE-HELLMAN ALGORITHM -------------

def diffie_hellman():
    print("\n--- DIFFIE-HELLMAN ALGORITHM ---")

    p = int(input("Enter prime p: "))
    g = int(input("Enter generator g: "))

    a = int(input("Enter A's private key: "))
    b = int(input("Enter B's private key: "))

    if p <= 1 or g < 0 or a < 0 or b < 0:
        print("Invalid input.")
        return

    # Calculate public keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Calculate shared secrets
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("\nDiffie-Hellman Results")
    print("A's Public Key:", A)
    print("B's Public Key:", B)
    print("Shared Secret at A:", key_A)
    print("Shared Secret at B:", key_B)
    print("Keys Match:", key_A == key_B)


# ---------------- ECC ALGORITHM ----------------

def ecc():
    print("\n--- ELLIPTIC CURVE CRYPTOGRAPHY (ECC) ---")

    p = int(input("Enter prime p: "))
    curve_a = int(input("Enter curve coefficient a: "))
    curve_b = int(input("Enter curve coefficient b: "))

    gx = int(input("Enter base point G x-coordinate: "))
    gy = int(input("Enter base point G y-coordinate: "))

    private_A = int(input("Enter A's private key: "))
    private_B = int(input("Enter B's private key: "))

    if p <= 2 or private_A < 0 or private_B < 0:
        print("Invalid input.")
        return

    G = (gx % p, gy % p)

    # Check whether a point lies on the curve
    def is_on_curve(point):
        if point is None:
            return True

        x, y = point

        return (
            (y * y - (x * x * x + curve_a * x + curve_b)) % p == 0
        )

    # Elliptic curve point addition and doubling
    def point_add(P1, P2):
        if P1 is None:
            return P2

        if P2 is None:
            return P1

        x1, y1 = P1
        x2, y2 = P2

        # A point plus its inverse equals infinity
        if x1 == x2 and (y1 + y2) % p == 0:
            return None

        # Point doubling
        if P1 == P2:
            denominator = (2 * y1) % p

            slope = (
                (3 * x1 * x1 + curve_a)
                * pow(denominator, -1, p)
            ) % p

        # Addition of two different points
        else:
            denominator = (x2 - x1) % p

            slope = (
                (y2 - y1)
                * pow(denominator, -1, p)
            ) % p

        x3 = (slope * slope - x1 - x2) % p
        y3 = (slope * (x1 - x3) - y1) % p

        return (x3, y3)

    # Scalar multiplication using double-and-add
    def scalar_mult(k, point):
        result = None
        current = point

        while k > 0:
            if k & 1:
                result = point_add(result, current)

            current = point_add(current, current)
            k >>= 1

        return result

    # Validate the base point
    if not is_on_curve(G):
        print("Invalid base point: G is not on the given curve.")
        return

    # Calculate public keys
    public_A = scalar_mult(private_A, G)
    public_B = scalar_mult(private_B, G)

    # Calculate shared secret points
    shared_A = scalar_mult(private_A, public_B)
    shared_B = scalar_mult(private_B, public_A)

    print("\nECC Results")
    print("Base Point G:", G)
    print("A's Public Key:", public_A)
    print("B's Public Key:", public_B)
    print("Shared Point at A:", shared_A)
    print("Shared Point at B:", shared_B)
    print("Shared Points Match:", shared_A == shared_B)


# ---------------- MAIN PROGRAM ----------------

def main():
    while True:
        print("\n========== CRYPTOGRAPHY ALGORITHMS ==========")
        print("1. RSA Algorithm")
        print("2. Diffie-Hellman Algorithm")
        print("3. ECC Algorithm")
        print("4. Run All Algorithms")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                rsa()

            elif choice == "2":
                diffie_hellman()

            elif choice == "3":
                ecc()

            elif choice == "4":
                rsa()
                diffie_hellman()
                ecc()

            elif choice == "5":
                print("Program terminated.")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except ValueError:
            print("Please enter valid integer values.")

        except ZeroDivisionError:
            print("Invalid parameters: modular inverse does not exist.")

        except TypeError:
            print("Invalid parameters for the cryptographic operation.")


if __name__ == "__main__":
    main()