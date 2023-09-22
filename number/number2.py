## RANDOM NUMBER
import random 

print("-------------------- TOGEL BERHADIAH --------------------")
progress = True;
while progress:
    print("Pilihan Menu: ")
    print("1. Main Tebak Togel")
    print("2. Keluar")
    pilihan = int(input("Pilih: "))

    if pilihan == 1:
        hasil = random.randrange(1, 10000)
        if (hasil % 2 == 1):
            print("Selamat! Anda menang (", hasil, ")")
            print('')
            print('')
        else:
            print("Anda kalah (", hasil, ") Silahkan coba kembali :)")
            print('')
            print('')
    elif pilihan == 2:
        print("Selamat! Berhasil Keluar dari Lingkaran Setan!")
        progress = False
    else:
        print("Input tidak dapat dimengerti, silahkan coba kembali")
        print('')
        print('')