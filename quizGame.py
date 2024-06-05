print("Selamat Datang di Quiz Game")

main = input("Apa kamu ingin main sekarang ?? ")

if main.lower() != "iya":
    quit()
    
print("Baiklah, Ayo Kita Main Sekarang")
score = 0

jawab = input("Berapa presiden yang ada di indonesia ?")
if jawab.lower() == "1":
    print("Asikkkk benar 🫡")
    score += 1
else :
    print("Owowow salah ternyata...")
    
jawab = input("Berapa jumlah provinsi di indonesia ?")
if jawab.lower() == "38":
    print("Asikkkk benar 🫡")
    score += 1
else :
    print("Owowow salah ternyata...")
    
jawab = input("Sebutkan pulau terluas di indonesia ?")
if jawab.lower() == "kalimantan":
    print("Asikkkk benar 🫡")
    score += 1
else :
    print("Owowow salah ternyata...")
    
jawab = input("Apa gunung terbesar di indonesia ?")
if jawab.lower() == "PuncakJava":
    print("Asikkkk benar 🫡")
    score += 1
else :
    print("Owowow salah ternyata...")
    
jawab = input("1 + 1 = ?")
if jawab.lower() == "11":
    print("Asikkkk benar 🫡")
    score += 1
else :
    print("Owowow salah ternyata...")

print()
print("Kamu mendapatkan " + str(score) + " jawaban yang benar")
print("Kamu mendapatkan " + str((score / 4) * 100) + "%.")

