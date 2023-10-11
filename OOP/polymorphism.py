from assets.helper import *

## example of 'polymorphism function'
# 1
Language = "Python"
print(len(Language))

# 2 (tuple)
food = ("Nasi Padang", "Gado-Gado", "Gudeg")
print(len(food))

# 3 (dict)
identity = {
    "nama" : "Daniel",
    "umur" : "9x2",
    "tanggal lahir" : "Hari Bulan Tahun" 
}
print(len(identity))

FreeSpace()

## Class Polymorphism
class Desktop:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu
    
    def mobility(self):
        print("Easy to bring anywhere at anytime!")

class Laptop:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def mobility(self):
        print("Sorry! Can't bring device to anywhere at anytime")

desktop = Desktop("Intel I9 Gen 13", "RTX 4050")
laptop = Laptop("Intel I7 Gen 13", "RTX 3050")

for i in (desktop, laptop):     # Accessed from the object that created from the class
    i.mobility()

FreeSpace()

## Class Polymorphism that contain Inheritance aspect
class Cloud:
    def __init__(self, data):
        self.data = data

    def getData(self):
        x = open(self.data, "r")
        print(x.read())

class PublicCloud(Cloud):
    pass

class PrivateCloud(Cloud):
    def getData(self):
        print("Cannot carelessly get the cloud data!")
        print("Because it's Private (you already know it lol)")
        ShowErrorCode(False)
        print(" ")
        
class HybridCloud(Cloud):
    def getData(self):
        print("Cannot carelessly get the cloud data!")
        print("Because Hybrid Cloud still use Private Cloud in it")
        ShowErrorCode(False)

UserOne = Cloud("D:/ExpertProgrammer/Languages/Python/Belajar/OOP/assets/readfiles.txt")
UserTwo = PublicCloud("D:/ExpertProgrammer/Languages/Python/Belajar/OOP/assets/readfiles.txt")
UserThree = PrivateCloud("D:/ExpertProgrammer/Languages/Python/Belajar/OOP/assets/readfiles.txt")
UserFour = HybridCloud("D:/ExpertProgrammer/Languages/Python/Belajar/OOP/assets/readfiles.txt")

for x in (UserOne, UserTwo, UserThree, UserFour):
    x.getData()

FreeSpace()


