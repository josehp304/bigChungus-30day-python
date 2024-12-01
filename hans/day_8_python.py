number=int(input("Enter number"))
count=0
for i in range (2,number):
     if number%i==0:
          count=1
          break
if count==1:
      print("The number is not a prime number")
else:
      print("The number is a prime number")                    