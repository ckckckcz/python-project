import random

user_menang = 0 
sistem_menang = 0

pilihan = ["batu", "kertas", "gunting"]

while True:
    user_input = input("Ketik Batu/Ketas/Gunting : ").lower()
    if user_input == "q":
        break
    
    if user_input not in pilihan:
        continue
    
    random_angka = random.randint(0,2)
    sistem_pilih = pilihan[random_angka]
    print("Sistem memilih", sistem_pilih + ".")
    
    if user_input == "batu" and sistem_pilih == "gunting":
        print("Kamu Menang !!!")
        user_menang += 1
    
    elif user_input == "kertas" and sistem_pilih == "batu":
        print("Kamu Menang !!!")
        user_menang += 1
        
    elif user_input == "gunting" and sistem_pilih == "kertas":
        print("Kamu Menang !!!")
        user_menang += 1
    
    else :
        print("Kamu Kalah !!!")
        sistem_menang += 1
        
print("===============================================")    
print("Kamu Menang", user_menang, "kali.")
print("Sistem Menang", sistem_menang, "kali.")
print("Terima Kasih Sudah Bermain !!!")