string = input("enter a word: ")
vowel_count = 0
for x in string:
    if(x in ["a","e","i","o","u"]):
        vowel_count += 1
print(vowel_count)