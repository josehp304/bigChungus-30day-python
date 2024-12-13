list1 = [int(num) for num in input("enter a list of numbers: ").split(",")]
list2 = [int(num) for num in input("enter another list of numbers: ").split(",")]
common_nums = []
for i in list1:
    for x in list2:
        if i == x:
            common_nums.append(i)

print (common_nums)