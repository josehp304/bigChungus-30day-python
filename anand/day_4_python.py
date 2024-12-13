string=input("Enter the string")
vowel="AEIOUaeiou"
count=0
for i in range (len(string)):
        if string[i] in vowel:
                count+=1
print("Number of vowels = ",count)                
