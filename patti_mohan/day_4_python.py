s=input("enter a word:")
vowels= "aeiouAEIOU"
count= sum(1 for char in s if char in vowels)
print("number of vowels =",count)
