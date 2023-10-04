### GLOBAL VARIABLES ###

## this is global variables, can be accessed everywhere (out and in a function)
nama = "Daniel Adi Pratama"
pesanan = "Indomie Rendang"
jumlahBarang = 10
hargaBarang = (jumlahBarang * 1000)

def dataPembayaran():
    print("Pelanggan:", nama + ";" + 
          "\nMembeli:", pesanan + ";", 
          "\nJumlah harga barang yang dibeli:", hargaBarang)
    print("TRANSACTION DONE!")

dataPembayaran()

print(" ")

## create variable that the name is same as the global variable
quote = "Saya Anak Tuhan"

def anakTetew():
    quote = "Saya ganteng dan berintelektual"
    print(quote) 

anakTetew() # Saya ganteng dan berintelektual
print(quote) # Saya Anak Tuhan

print(" ")

## makes local variable inside function to global variable (while the position is still inside a function)
# 'global' keyword
def bankAccount():
    global bank
    bank = "Semarang Bank"

bankAccount()
print("I save my money in", bank)
''' 
before you can call global variable inside a function,
you must call the function first in order to call the global variable inside of it
'''

print(" ")

## override the (literally) global variable by 'global' variable inside function
breakfast = "Bubur diaduk"

def BreakfastMenu():
    global breakfast 
    breakfast = "Nasi Uduk"

BreakfastMenu()
print("Saya sarapan hari ini dengan", breakfast) # Nasi Uduk

print(" ")