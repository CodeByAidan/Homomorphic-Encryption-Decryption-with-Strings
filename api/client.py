import socket
import numpy as np
import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))
import rlwe_he_scheme_updated as rlwe_updated

PLAINTEXT = "Testing! Hello World!"


if __name__ == "__main__":
    host = 'localhost'
    port = 12345

    n = 2 ** 3
    q = 2 ** 14
    t = 2

    T = int(np.sqrt(q))
    p = q ** 3
    poly_mod = np.array([1] + [0] * (n - 1) + [1])
    std1 = 1
    std2 = 1

    pk, sk = rlwe_updated.keygen(n, q, poly_mod, std1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send the secret key to the server
    sk_bytes = sk.tobytes()
    client_socket.sendall(sk_bytes)
    print("Sent secret key to server")

    binary_vector = [format(ord(char), '08b') for char in PLAINTEXT]

    ciphertexts = []
    for binary_value in binary_vector:
        pt = [int(bit) for bit in binary_value]
        ct = rlwe_updated.encrypt(pk, n, q, t, poly_mod, pt, std1)
        ciphertexts.append(ct)

    for ct in ciphertexts:
        ct_combined = np.concatenate((ct[0], ct[1]))
        client_socket.sendall(ct[0].tobytes())
        client_socket.sendall(ct[1].tobytes())

    print("Sent ciphertexts to server")

    client_socket.close()
