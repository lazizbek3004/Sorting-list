# finding the largest and smallest number in a list
# making a list using the number which we get from user
# in compiler

list = []
# asking three numbers 
times = 3 
while times > 0:
    num = int(input("Enter a number for list: "))
    times-=1
    list.append(num)

def find_largest(List):
    largest = List[0]
    for i in list:
        if i > largest:
            largest = i
            
    return largest
    
def find_smallest(List):
    smallest = List[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest


print(f"The largest num in {list} is {find_largest(list)}")
print(f"The smallest num in {list} is {find_smallest(list)}")
