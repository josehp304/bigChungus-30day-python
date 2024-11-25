list1=[]
list2=[]
list3=[]
n=int(input("Enter the total number of terms in the first list"))
print("Enter numbers in first list")
for i in range (n):
     number=input()
     list1.append(number)
n1=int(input("Enter the total number of terms in the second list"))     
print("Enter numbers in second list")     
for i in range (n1):
      number2=input()
      list2.append(number2)
for i in range (n):
       for j in range(n1):
             if list1[i]==list2[j]:
                    list3.append(list1[i])
print("First list =",list1)
print("Second list =",list2)
print("Common terms are :",list3)    