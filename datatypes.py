### DATA TYPES ###

## Built-in Data Types
# (not specific)
def FreeSpace():
    print(" ")

def firstEx():
    a = "Halo, nama saya Daniel dan saya ganteng dan berintelektual" # string
    print(a)
    print(type(a))
    FreeSpace()

    b = 10                                                           # int
    print(b)
    print(type(b))
    FreeSpace()

    c = 10.8                                                         # float
    print(c)
    print(type(c))
    FreeSpace()

    d = 55J                                                          # complex
    print(d)
    print(type(d))
    FreeSpace()

    e = ["McDonald", "KFC", "Hokben"]                                # list
    print(e)
    print(type(e))
    FreeSpace()

    f = ("McDonald", "KFC", "Hokben")                                # tuple
    print(f)
    print(type(f))
    FreeSpace()

    g = range(2, 10)                                                 # range
    print(g)
    print(type(g))
    FreeSpace()

    h = {"nama" : "Daniel", "umur" : 18}                             # dict (like map, has key and value)
    print(h)
    print(type(h))
    FreeSpace()

    i = {"McDonald", "KFC", "Hokben"}                                # set
    print(i)
    print(type(i))
    FreeSpace()

    j = frozenset({"McDonald", "KFC", "Hokben"})                     # frozenset
    print(j)
    print(type(j))
    FreeSpace()

    k = True                                                         # bool
    print(k)
    print(type(k))
    FreeSpace()

    l = b"Daniel Adi Pratama"                                        # bytes
    print(l)
    print(type(l))
    FreeSpace()

    m = bytearray(10)                                                # bytearray
    print(m)
    print(type(m))
    FreeSpace()

    n = memoryview(bytes(10))                                        # memoryview
    print(n)
    print(type(n))
    FreeSpace()

    o = None                                                         # NoneType
    print(o)
    print(type(o))
    FreeSpace()

## How to Specific directly to the data type value
def secondEx():
    satu = str("Halo saya Daniel")
    print(satu)
    print(type(satu))
    FreeSpace()

    dua = int(10)
    print(dua)
    print(type(dua))
    FreeSpace()

    tiga = float(15.6)
    print(tiga)
    print(type(tiga))
    FreeSpace()

    empat = complex(3+10J)
    print(empat)
    print(type(empat))
    FreeSpace()

    lima = list(("Badminton", "Basketball", "Volleyball"))
    print(lima)
    print(type(lima))
    FreeSpace()

    enam = tuple(("Badminton", "Basketball", "Volleyball"))
    print(enam)
    print(type(enam))
    FreeSpace()

    tujuh = range(2, 16, 4)
    print(tujuh)
    print(type(tujuh))
    FreeSpace()

    delapan = dict(Username="Daniel", PhoneNumber="0123456789")
    print(delapan)
    print(type(delapan))
    FreeSpace()

    sembilan = set(("Coca-Cola", "Fanta", "Sprite", "Pepsi"))
    print(sembilan)
    print(type(sembilan))
    FreeSpace()

    sepuluh = frozenset(("Coca-Cola", "Fanta", "Sprite", "Pepsi"))
    print(sepuluh)
    print(type(sepuluh))
    FreeSpace()

    sebelas = bool(-10)
    print(sebelas)
    print(type(sebelas))
    FreeSpace()

    duaBelas = bytes(20)
    print(duaBelas)
    print(type(duaBelas))
    FreeSpace()

    tigaBelas = bytearray(20)
    print(tigaBelas)
    print(type(tigaBelas))
    FreeSpace()

    empatbelas = memoryview(bytes(20))
    print(empatbelas)
    print(type(empatbelas))
    FreeSpace()

# For Testing
secondEx()