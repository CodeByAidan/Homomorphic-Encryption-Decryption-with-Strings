import socket
import numpy as np
import os
import sys
import datetime

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

import rlwe_he_scheme_updated as rlwe_updated

def decrypt_ciphertexts(ciphertexts, sk, n, q, t, poly_mod):
    decrypted_binary_vectors = []
    for ct in ciphertexts:
        ct_combined = np.concatenate((ct[0], ct[1]))
        decrypted_value = rlwe_updated.decrypt(
            sk, n, q, t, poly_mod, ct_combined)
        decrypted_binary_vectors.append(decrypted_value)
    return ''.join(
        [
            chr(int(''.join(map(str, binary_vector)), 2))
            for binary_vector in decrypted_binary_vectors
        ]
    )


if __name__ == "__main__":
    host = 'localhost'
    port = 12345

    n = 2 ** 3
    q = 2 ** 14
    t = 2

    poly_mod = [1] + [0] * (n - 1) + [1]

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("Server is listening for incoming connections...")

    client_socket, _ = server_socket.accept()

    # Receive the secret key from the client
    sk_bytes = client_socket.recv(4096)
    sk = np.frombuffer(sk_bytes, dtype=np.int64)

    received_data = b''
    while True:
        if data := client_socket.recv(4096):
            received_data += data

        else:
            break
    print("Received data")

    ciphertexts = []
    chunk_size = n * 8 * 2  # 8 * 8 * 2 = 128 bytes
    for i in range(0, len(received_data), chunk_size):
        ct_part1 = np.frombuffer(received_data[i:i + n * 8], dtype=np.int64)
        ct_part2 = np.frombuffer(
            received_data[i + n * 8:i + 2 * n * 8], dtype=np.int64)
        ciphertexts.append((ct_part1, ct_part2))
    print(ciphertexts)

    decrypted_binary_vectors = []

    for ct in ciphertexts:
        decrypted_value = rlwe_updated.decrypt(sk, n, q, t, poly_mod, ct)
        decrypted_binary_vectors.append(decrypted_value)
    print(decrypted_binary_vectors)

    decrypted_text = ''.join([chr(int(''.join(map(str, binary_vector)), 2))
                             for binary_vector in decrypted_binary_vectors])

    print(f"Decrypted text: {decrypted_text}")
    print(f"Character count: {len(decrypted_text)}")

    server_socket.close()

    now = datetime.datetime.now()
    os.chdir(os.path.dirname(__file__))
    os.makedirs("log", exist_ok=True)
    os.chdir("log")

    with open("output.log", "a", encoding="utf-8") as log_file:
        log_file.write(
            f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond} [SERVER] Received data: {received_data}\n")

        ciphertexts_str = "["
        for ct in ciphertexts:
            ct_str = "(array(" + ', '.join(map(str, ct[0])) + "), array(" + ', '.join(map(str, ct[1])) + "))"
            ciphertexts_str += f"{ct_str}, "
        ciphertexts_str = ciphertexts_str.rstrip(", ") + "]"

        log_file.write(
            f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond} [SERVER] Ciphertexts: {ciphertexts_str}\n")
        log_file.write(
            f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond} [SERVER] Decrypted binary vectors: {decrypted_binary_vectors}\n")
        log_file.write(
            f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond} [SERVER] Decrypted text: {decrypted_text}\n")
        log_file.write(
            f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond} [SERVER] Character count: {len(decrypted_text)}\n")
