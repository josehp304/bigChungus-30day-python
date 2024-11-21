nums = input("enter the numbers: ")
num_list = [int(num) for num in nums.split(" ")]
odd = []
even =[]

for i in range(len(num_list)):
    if num_list[i]%2 == 0:
       even.append(num_list[i])
    else:
        odd.append(num_list[i]) 
print("odd numbers are ", odd)
print("even numbers are ", even)