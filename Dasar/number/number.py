### PYTHON NUNMBERS ###

def FreeSpace():
    print('')
    print("-----------------------------------------")
    print('')

## brief example:
iniInt = int(50)        # int
iniFloat = 31.98        # float
iniComplex = 4+5j       # complex

print(iniInt, "\t", type(iniInt))
print(iniFloat, "\t", type(iniFloat))
print(iniComplex, "\t", type(iniComplex))

FreeSpace()

## int
int1 = 32
int2 = 2043240237403274
int3 = -3434

print(int1, "\t\t\t", type(int1))
print(int2, "\t", type(int2))
print(int3, "\t\t\t", type(int3))

FreeSpace()

## float
float1 = 34.56
float2 = 1.2
float3 = -33.778

print(float1, "\t\t", type(float1))
print(float2, "\t\t", type(float2))
print(float3, "\t", type(float3))

# e/E is scientific number that indicate the power of 10
EFloat1 = 35e3 
EFloat2 = 12E4
EFloat3 = -67.3e10

print('')

print(EFloat1, "\t\t", type(EFloat1))
print(EFloat2, "\t\t", type(EFloat2))
print(EFloat3, "\t", type(EFloat3))

FreeSpace()

## complex, with j/J as the imaginary part
complex1 = 6+23J
complex2 = 9j
complex3 = -145j

print(complex1, "\t", type(complex1))
print(complex2, "\t\t", type(complex2))
print(complex3, "\t", type(complex3))

FreeSpace()

## TYPE CONVERSION
A = int(140)        # int
B = float(35.2)     # float
C = complex(55j)    # complex

