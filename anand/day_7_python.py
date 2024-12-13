num=int(input("Enter the total number of terms"))
original=[]
print("Enter the numbers")
for i in range(num):
      number=int(input())
      original.append(number)
set1=set(original)
unique_terms=list(set1)
print("Original= ",original)
print("Unique terms = ",unique_terms)      
