### VARIABLES OUTPUT ###

# Single Variable
nama = "Daniel"
print(nama)
absen = 10
print(absen)

print(" ")

## Multiple Variables
# separated by comma ',' character (THE BEST PRACTICE!!!!!)
NamaDepan = "Daniel"
NamaBelakang = "Adi Pratama"
print(NamaDepan, NamaBelakang)

print(" ")

# separated by '+' character
perguruan_tinggi = "POLINES "       # '+' character doesn't add space automatically, so we must add the space manually
prodi = "TRK "
kelas = "TI-1A"
print(perguruan_tinggi + prodi + kelas)

print(" ")

# '+' as a mathemathical operator
angkaPertama = 100
angkaKedua = 50
jumlah = angkaPertama + angkaKedua
print(jumlah)

print(' ')

# '+' cannot be used to combine string and number data type
#nama = "Adi"
#umur = 18
#identitas = (nama + umur)       # TypeError: can only concatenate str (not "int") to str
#print(identitas) 