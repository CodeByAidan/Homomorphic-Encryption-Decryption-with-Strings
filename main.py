"""
Thank you to the author of the original code:
    - Madalina Bolboceanu (@mbolboceanu)

This code is an updated version of the original code, which can be found here:
    - https://github.com/bit-ml/he-scheme
"""

import rlwe_he_scheme_updated as rlwe_updated
import numpy as np

if __name__ == '__main__':
    # Scheme's parameters
    # polynomial modulus degree
    n = 2 ** 3
    # ciphertext modulus
    q = 2 ** 14
    # plaintext modulus
    t = 2
    # base for relin_v1
    T = int(np.sqrt(q))
    # modulusswitching modulus
    p = q ** 3

    # polynomial modulus
    poly_mod = np.array([1] + [0] * (n - 1) + [1])

    # standard deviation for the error in the encryption
    std1 = 1
    # standard deviation for the error in the evaluateKeyGen_v2
    std2 = 1

    # Keygen
    pk, sk = rlwe_updated.keygen(n, q, poly_mod, std1)

    # EvaluateKeygen_version1
    rlk0_v1, rlk1_v1 = rlwe_updated.evaluate_keygen_v1(sk, n, q, T, poly_mod, std1)

    # EvaluateKeygen_version2
    rlk0_v2, rlk1_v2 = rlwe_updated.evaluate_keygen_v2(sk, n, q, poly_mod, p, std2)

    # Encrypting "Hello world" as binary vectors
    plaintext = "Hello world"
    # Convert each character to 8-bit binary
    binary_vector = [format(ord(char), '08b') for char in plaintext]

    print(f"[+] Plaintext: {plaintext}\n")
    print(f"[+] Binary vectors: {binary_vector}\n")

    # Encrypting the binary vectors
    ciphertexts = []
    for binary_value in binary_vector:
        pt = [int(bit) for bit in binary_value]
        ct = rlwe_updated.encrypt(pk, n, q, t, poly_mod, pt, std1)
        ciphertexts.append(ct)

    print(f"[+] Ciphertexts: {ciphertexts}\n")

    # Decrypting the binary vectors and converting back to text
    decrypted_binary_vectors = []
    for ct in ciphertexts:
        decrypted_value = rlwe_updated.decrypt(sk, n, q, t, poly_mod, ct)
        decrypted_binary_vectors.append(decrypted_value)

    print(f"[+] Decrypted binary vectors: {decrypted_binary_vectors}\n")

    decrypted_text = ''.join([chr(int(''.join(map(str, binary_vector)), 2)) for binary_vector in decrypted_binary_vectors])

    print(f"[+] Decrypted text: {decrypted_text}")
