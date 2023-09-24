### PYTHON STRING ###

def FreeSpace():
    print('')
    print('')

singleQuote = 'Daniel'
doubleQuote = "Daniel"
print(singleQuote, "\t", doubleQuote)

FreeSpace()

## Multiline String
# 3-single quote
singleLoremIpsum = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(singleLoremIpsum)

FreeSpace()

# 3-double quote
doubleLoremIpsum = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(doubleLoremIpsum)

FreeSpace()

## String is Array
crush = "Tirza"
print("Huruf 1:", crush[0])
print("Huruf 2:", crush[1])
print("Huruf Terakhir:", crush[4])

FreeSpace()

## Looping through a String
favCar = "Lancer Evo"
for x in favCar:
    print(x)

FreeSpace()

## String length
food = "Bacon"
print("My Favourite food is:", food + "; with length of word are", len(food))

FreeSpace()

## Check string, "in" and "not in"
kelas = "TI"
print("TI" in kelas, "IK" not in kelas)

FreeSpace()

# Checking with If (in)
subKelas = input("Masukkan subkelas anda: ")
if "1A" in subKelas:
    print("Anda Masuk Kelas TI-1A")
elif "1B" in subKelas:
    print("Anda Masuk Kelas TI-1B")
elif "1C" in subKelas:
    print("Anda Masuk Kelas TI-1C")
else:
    print("Kamu anak TRK apa bukan?")

FreeSpace()

# Checking with if (not in)
matKul = input("Masukkan kata kunci: ")
if "Pemrograman" not in matKul:
    print("Selain Pak Prayit dan Bu Wikta")
else:
    print("Matkulnya Pak Prayit dan Bu Wikta")