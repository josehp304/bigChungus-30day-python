def fact(number):
     if number==1:
           return 1
     else:
            return number*fact(number-1)
num=int((input("Enter a number")))
print(fact(num))     