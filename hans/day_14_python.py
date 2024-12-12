# Program to check whether the given number is a valid mobile number or not using functions.

#            Rules:

#               1.       Every number should contain exactly 10 digits.

#               2.       The first digit should be 7 or 8 or 9
def checking(ph_No):
     num=ph_No
     count=0
     while(num>0):
           count+=1
           num=num//10
     if count ==10 and (ph_No//10**9==7 or ph_No//10**9==8 or ph_No//10**9==9):
            return True
     else:
            return False
Number=int(input("Enter a phone number"))
if checking(Number)==True:
       print("Valid Number")
else :
       print("Invalid Number")                 