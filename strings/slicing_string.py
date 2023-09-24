### SLICING STRING ###

## Basic Learning
# Slicing from the start
couple = "Daniel and Tirza"
print(couple[:6])           # Daniel

# Slicing to the end    
print(couple[11:])          # Tirza

# Slicing with negative index number
print(couple[-16:-10])      # Daniel
print(couple[-5:])          # Tirza

print('')
print('')

## Data Mahasiswa/i
nama = input("Masukkan Nama Anda: ")
nim = input("Masukkan NIM Anda: ")
angkatan = []
gender = input("Masukkan Gender Anda [L/P]: ")

if gender == 'L':
    gender = "Laki-Laki"
elif gender == 'P':
    gender = "Perempuan"
else:
    print("Data tidak dimengerti")

if len(nim) == 8:
    angkatan.append(nim[3:5])
    print("Nama:", nama, "\nNIM:", nim, "\nJenis Kelamin:", gender, "\nAngkatan:", angkatan[0])
else:
    print("NIM tidak valid")

print('')
print('')