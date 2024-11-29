list=[]
n=int(input("enter the number of values in the list "))
for i in range (0,n):
    value=int(input("enter the number "))
    list.append(value)
print("list = ",list)
list.sort()
print("list in asending order = ",list)
if n%2==0:
    print("middle numbers",list[n//2-1],"\b,",list[n//2])
else:
    print("middle number",list[n//2])
