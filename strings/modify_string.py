### MODIFY STRING ###

# Helper Method
def freeSpace():
    print('')

## Uppercase
nama = "Daniel Adi Pratama"
namaSlice = nama[0:6] 
print(namaSlice.upper())

freeSpace()

## Lowercase
crush = "TIRZA NADYA WIBOWO"
print(crush.lower())

freeSpace()

## Remove Whitespace, before and after the actual text, not in the middle of words like space 
kalimat1 = "  Saya suka makan  "        
print(kalimat1)
print(kalimat1.strip())
kalimat2 = "Saya   suka   makan"        # No difference
print(kalimat2)         
print(kalimat2.strip())

freeSpace()

## Replace String
namaSaya = "Daniel"
print(namaSaya.replace('D', 'T'))

freeSpace()

## Split String
sayaDanCrush = "Daniel Tirza"
splitResult = sayaDanCrush.split()
print(splitResult)

freeSpace()