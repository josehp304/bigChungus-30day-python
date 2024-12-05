def even(list1):
     list3=[]
     for j in range(len(list1)):
           if list1[j]%2==0:
              list3.append(list1[j])             
     print(list3)            
n=int(input("Enter the number of terms"))
list2=[]
print("Enter numbers")
for i in range(n):
       num=int(input())
       list2.append(num)
even(list2)      