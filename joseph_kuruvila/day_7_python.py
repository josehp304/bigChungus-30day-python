list1 = [int(num) for num in input("enter a list of numbers: ").split(",")]
unique_list = list(set(list1))
print (unique_list)