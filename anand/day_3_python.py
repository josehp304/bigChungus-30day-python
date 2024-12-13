n=int(input("Enter the total number of digits"))
num=[]
print("Enter ",n," numbers")
for i in range (n):
    number=int(input())
    num.append(number)
print("Numbers =",num)
num.sort()
print("Numbers in ascending order=",num)     
if len(num)%2!=0:
      print("Middle term=",num[n//2])
else:
      print("Middle terms are:",num[(n-1)//2],"and",num[((n-1)//2)+1])
