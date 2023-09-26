### STRING METHODS ###

def FreeSpace():
    print('')

## capitalize() method
# to capitalize the first character
FirstSentence = "makan NasGor"      # Makan nasgor
CapitalizeFirstSentence = FirstSentence.capitalize()

FirstExample = "15000 is the price of NasGor"     # no changes
CapitalizeFirstExample = FirstExample.capitalize()
print(CapitalizeFirstSentence, "\t", CapitalizeFirstExample)

FreeSpace()

## casefold() method, more powerful than lower() method
# to convert all letters into lowercase format
SecondSentence = "I'm Currently Reading Monogatari Series Light Novel"
CasefoldSecondSentence = SecondSentence.casefold()
print("Status: ", CasefoldSecondSentence)

FreeSpace()

## center(length, character) method
# character argument is optional (default is ' ') -> to fill in the missing space on each side
ThirdSentence = "Di Tengah"
CenterThirdSentence = ThirdSentence.center(20)      # for ex: taking up space of 20 characters
print(CenterThirdSentence)
print("ABCDEFGHIJKLMNOPQRST")       # testing to check if the 20 characters space is correct

FourthSentence = "On Center"
CenterFourthSentence = FourthSentence.center(20, "/")
print(CenterFourthSentence)

FreeSpace()

## count(value, start, end) method
# to count the number of times the specified word appears in a string 
'''
value is required. The value we want to search
start is optional. Default is start at 0
end is optional. Default is the end of a string
'''
FifthSentence = "Tirza is my Crush, Tirza will be my GF, and Tirza will be my Wife"
CountFifthSentence = FifthSentence.count("Tirza")
print(CountFifthSentence)       # 3

CountFifthSentence2 = FifthSentence.count("Tirza", 7, 24)
print(CountFifthSentence2)      # 1

FreeSpace()

## encode(encoding=encoding, errors=errors) method
'''
encoding: Optional. A String specifying the encoding to use. Default is UTF-8
errors: Optional. Such as: "backslashreplace", "ignore", "namereplace", "replace", "xmlcharrefreplace"
'''
SixthSentence = "My name is Ståle"

print(SixthSentence.encode(encoding="ascii",errors="backslashreplace"))
print(SixthSentence.encode(encoding="ascii",errors="ignore"))
print(SixthSentence.encode(encoding="ascii",errors="namereplace"))
print(SixthSentence.encode(encoding="ascii",errors="replace"))
print(SixthSentence.encode(encoding="ascii",errors="xmlcharrefreplace"))

FreeSpace()

## endswith(value, start, end) method, arguments used are same with count() function's arguments
'''
value: Required. The value to check if the string ends with
start: Optional. An Integer specifying at which position to start the search
end: Optional. An Integer specifying at which position to end the search
'''
SeventhSentence = "This is my Bag."
EndsWithSeventhSentence = SeventhSentence.endswith("Bag.")
print(EndsWithSeventhSentence)      # True

EndsWithSeventhSentence2 = SeventhSentence.endswith("Bag", 1, 6)
print(EndsWithSeventhSentence2)     # False

FreeSpace()

## expandtabs(tabsize) method
'''
tabsize: Optional. A number specifying the tabsize. Default tabsize is 8
'''
EighthSentence = "T\ti\tr\tz\ta"
print(EighthSentence.expandtabs())
print(EighthSentence.expandtabs(0))
print(EighthSentence.expandtabs(2))
print(EighthSentence.expandtabs(4))
print(EighthSentence.expandtabs(6))
print(EighthSentence.expandtabs(8))
print(EighthSentence.expandtabs(10))

FreeSpace()

## find() method
'''
value: Required. The value to search for
start: Optional. Where to start the search. Default is 0
end: Optional. Where to end the search. Default is to the end of the string
'''
NinethSentence = "Ini Adalah Hamburger"
print(NinethSentence.find("Hamburger"))     # 11, start from index zero
print(NinethSentence.find("Hamburger", 1, 5))     # -1 
# print(NinethSentence.index("Hamburger", 1, 5))     # result Exception: substring not found

## and many more String Method