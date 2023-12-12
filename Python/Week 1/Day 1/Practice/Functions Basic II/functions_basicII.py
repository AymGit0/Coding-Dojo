def countdown(num):
    array=[]
    for i in range(0,num+1):
        array.append(num-i)
    return array

arr1=countdown(5)

def print_and_return(array):
    print(array[0])
    return array[1]

def first_plus_length(array):
    return array[0]+len(array)

def values_greater_than_second(array):
    newarray=[]
    if len(array)<2:
        return False
    else:
        for el in array:
            if el>array[1]:
                newarray.append(el)
        print(len(newarray))
        return newarray


def length_and_value(size, value):
    newarray=[]
    for i in range(0,size):
        newarray.append(value)
    return newarray

print(countdown(5))
print(print_and_return([1,2]))
print(first_plus_length([1,2,3,4,5]))
print(values_greater_than_second([5,2,3,2,1,4]))
print( values_greater_than_second([3]) )
print(length_and_value(4,7))
print(length_and_value(6,2))