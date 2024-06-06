import random

top_of_range = input("Masukkan sebuah angka : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <- 0:
        print("Ei ! jangan berikan angka 0, lain kali berikan angka diatas 0")
        quit()    
else:
    print("Lain kali berikan angka, jangan asal enter")
    quit()

random_angka = random.randint(0, top_of_range)
tebak = 0

while True:
    tebak += 1
    user_tebak = input("Berikan tebakan : ")
    if user_tebak.isdigit():
        user_tebak = int(user_tebak)
    else:
        print("Lain kali berikan angka, jangan asal enter")
        continue
    
    if user_tebak == random_angka:
        print("Anjay bener !!!!!!!")
        break
    elif user_tebak > random_angka:
        print("Masih jauh angkamu")
    else:
        print("Malah semakin bawah angkamu")

print("Anjay, kamu berhasil menebak", tebak, "tebakan")   