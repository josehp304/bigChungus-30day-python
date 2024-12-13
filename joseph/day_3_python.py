list =[None]
try:
    list = [int(num) for num in input("enter a list of numbers: ").split(" ") if int(num)>0]
except ValueError as e:
    print(f"an error occured:{e}")

if len(list)%2 ==0:
    print(f"middle values are:{list[(len(list)//2)-1]},{list[len(list)//2]}")
else:
    print(f"middle value is: {list[len(list)//2]}")


