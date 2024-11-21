n=int(input("Enter total number of digits"))
num=[]
even=[]
odd=[]
print("Enter ",n," numbers")
for i in range (n):
      number=int(input())
      num.append(number)
print(num) 
for i in range (0,n):
       if num[i]%2==0 :
             even.append(num[i])
       else:
              odd.append(num[i])             
print("Odd :",odd)
print("Even :",even)       
