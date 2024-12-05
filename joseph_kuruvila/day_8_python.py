num = int(input("enter a number: "))
def check_prime(n):
    key = 0 
    for i in range(1,n):
        if n%i == 0 :
            key+=1
    if key>1:
        print("not prime")
    else:
        print("prime")
check_prime(num)