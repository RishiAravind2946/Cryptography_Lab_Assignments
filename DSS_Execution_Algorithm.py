import hashlib

# DSS (DSA) Algorithm

# Read input parameters
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
k = int(input("Enter nonce k: "))
message = input("Enter message: ")

# Validate parameters
if (p - 1) % q != 0 or not (1 < g < p):
    raise ValueError("Invalid DSS parameters.")

if pow(g, q, p) != 1:
    raise ValueError("Invalid generator g.")

if not (1 <= x < q and 1 <= k < q):
    raise ValueError(
        "Private key and nonce must be between 1 and q-1."
    )

# Generate public key
y = pow(g, x, p)

# Calculate message hash
hash_value = int.from_bytes(
    hashlib.sha256(message.encode()).digest(), "big"
) % q

# Generate digital signature
r = pow(g, k, p) % q

if r == 0:
    raise ValueError("Invalid nonce. Choose another k.")

s = (pow(k, -1, q) * (hash_value + x * r)) % q

if s == 0:
    raise ValueError("Invalid nonce. Choose another k.")

print("\n--- DSS Digital Signature ---")
print("Public key:", y)
print("Hash value:", hash_value)
print("Signature (r, s):", (r, s))

# Verify digital signature
w = pow(s, -1, q)
u1 = (hash_value * w) % q
u2 = (r * w) % q

v = (
    (pow(g, u1, p) * pow(y, u2, p)) % p
) % q

print("Verification value:", v)

if v == r:
    print("Digital signature verified successfully.")
else:
    print("Digital signature verification failed.")