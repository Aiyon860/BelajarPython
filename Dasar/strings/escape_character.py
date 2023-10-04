### ESCAPE CHARACTER ###

def free_space():
    print('')

## to use double-quote inside double-quote, we must put: \" text \"
# Example 1
quote = "Saya adalah \"Akar\""
print(quote)

free_space()

# Example 2 (backslash character)
sentence_one = "Ini adalah karakter backslash \"\\\""
print(sentence_one)

free_space()

# Example 3 (new line)
sentence_two = "Give a new line: \nHalo, saya Daniel"
print(sentence_two)

free_space()

# Example 4 (\r is remove the words in front of the " \r ")
sentence_three = "Saya berkuliah\rdi Cuy University"
print(sentence_three)

free_space()

# Example 5 (giving tab)
sentence_empat = "Nama:\tDaniel"
print(sentence_empat)

free_space()

# Example 6 (no space between words)
sentence_lima = "Ini\badalah\bkalimat\btanpa\bspasi"
print(sentence_lima)

free_space()

# Example 7 (gatau gunanya buat apa)
sentence_enam = "Ini adalah form feed \f"
print(sentence_enam)

# Example 8 (Hex value)
sentence_tujuh = "\x44\x61\x6E\x69\x65\x6C"
print(sentence_tujuh)       # Daniel
print("\x54\x69\x72\x7a\x61")       # Tirza

free_space()

# Example 9 (Octal value)
sentence_delapan = "\144\141\156\151\145\154"
print(sentence_delapan)     # daniel
print("\164\151\162\172\141")       # tirza