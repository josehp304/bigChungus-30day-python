list=[1,2,3,4,5,6,7,8,9,10]
x=[]
y=[]
for i in range(len(list)):
  if list[i]%2 ==0:
    x.append(list[i])
  else:
    y.append(list[i])
print(x,y)