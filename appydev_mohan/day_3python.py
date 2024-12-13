def find_middleterm(numbers):
    numbers.sort()
    middleindex=len(numbers)//2
    if len(numbers)%2 == 0:
        return (numbers[middleindex -1] +numbers[middleindex])/2
    else:
            return numbers[middleindex]
inputnumbers= input("enter a list of numbers: ")
numbers = list(map(int,inputnumbers.split()))
middleterm=find_middleterm(numbers)
print("sorted list:",numbers)
print("middle term:",middleterm)