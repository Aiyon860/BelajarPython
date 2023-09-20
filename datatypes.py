### DATA TYPES ###

## Built-in Data Types
# (not specific)
def FreeSpace():
    print(" ")

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

g = range(2, 10)                                                    # range
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