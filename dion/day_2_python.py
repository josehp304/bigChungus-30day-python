list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
for n in list:
    if n % 2 == 0:
        even.append(n)  
    else:
        odd.append(n)  
print("odd:", odd)
print("even:", even)