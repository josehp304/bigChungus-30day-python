def seperate_oddeven(numbers):
    oddnumbers=[num for num in numbers if num % 2 !=0]
    evennumbers=[num for num in numbers if num % 2 ==0]
    return oddnumbers, evennumbers
inputnumbers= input("enter a list of numbers seperated by spaces:")
numbers = list(map(int,inputnumbers.split()))
oddnumbers, evennumbers = seperate_oddeven(numbers)
print("odd numbers:",oddnumbers)
print("even numbers:",evennumbers)