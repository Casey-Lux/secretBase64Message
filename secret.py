#!/usr/bin/env python3
import argparse
import base64
import hashlib
import os
from cryptography.fernet import Fernet


# =========================
# Crypto core
# =========================

def derive_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)


def encrypt(data: bytes, password: str) -> bytes:
    key = derive_key(password)
    return Fernet(key).encrypt(data)


def decrypt(data: bytes, password: str) -> bytes:
    key = derive_key(password)
    return Fernet(key).decrypt(data)


# =========================
# IO helpers
# =========================

def read_input(source: str) -> bytes:
    if os.path.isfile(source):
        with open(source, "rb") as f:
            return f.read()
    return source.encode()


def write_output(source: str, data: bytes, decrypting=False):
    if os.path.isfile(source):
        out = source.replace(".secret", "") if decrypting else source + ".secret"
        with open(out, "wb") as f:
            f.write(data)
        print(f"[+] Archivo generado: {out}")
    else:
        print(data.decode())


# =========================
# Main
# =========================

def main():
    parser = argparse.ArgumentParser(description="Encrypt / Decrypt using password + Base64")
    parser.add_argument("-c", "--crypt", action="store_true", help="Encrypt")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt")
    parser.add_argument("-p", "--password", required=True, help="Password")
    parser.add_argument("-s", "--source", required=True, help="String or file")

    args = parser.parse_args()

    if args.crypt == args.decrypt:
        parser.error("Debes usar -c o -d (uno solo)")

    data = read_input(args.source)

    try:
        if args.crypt:
            result = encrypt(data, args.password)
            write_output(args.source, result)
        else:
            result = decrypt(data, args.password)
            write_output(args.source, result, decrypting=True)

    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    main()
