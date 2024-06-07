import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

def lihat():
    try:
        with open('kataSandi.txt', 'r') as f:
            print("\nKata Sandi yang Disimpan :\n" + "-"*40)
            print(f"{'User':<20} | {'Password':<20}")
            print("-" * 40)
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print(f"{user:<20} | {decrypted_pass:<20}")
            print("-" * 40 + "\n")
    except FileNotFoundError:
        print("Tidak Ada Kata Sandi yang Disimpan.\n")

def tambah():
    name = input('Nama Akun : ')
    pwd = input("Kata Sandi : ")

    with open('kataSandi.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Kata Sandi Berhasil Ditambahkan !\n")

while True:
    mode = input("Ingin menambahkan akun baru atau melihat akun yang sudah ada ? ( lihat, tambah ) ketik q untuk keluar ").lower()
    if mode == "q":
        break

    if mode == "lihat":
        lihat()
    elif mode == "tambah":
        tambah()
    else:
        print("Pilihan tidak diketahui.\n")
        continue
