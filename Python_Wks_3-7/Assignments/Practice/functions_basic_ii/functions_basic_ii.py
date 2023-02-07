# Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element).
def countdown(number):
    
    new_list = []
    for x, y in zip(range(len(range(number+1))),range(number,-1,-1)):
        # print(x)
        # print(y)
        new_list.append(y)
    
    return new_list
print(countdown(5))

# Create a function that will receive a list with two numbers.
# Print the first value and return the second.
def printReturn(array):
    a = array[0]
    b = array[1]
    
    print(a)
    return b
    
print(printReturn([1,2]))

# Create a function that accepts a list and returns
# the sum of the first value in the list plus the list's length.
list_1 = [0,1,2,3,4,5,6,7,8,9]

def firstPlusLength(list):
    
    return list[0] + len(list)
print(firstPlusLength(list_1))

# Write a function that accepts a list and creates a new list
# containing only the values from the original list that
# are greater than its 2nd value. Print how many values
# this is and then return the new list. If the list has
# less than 2 elements, have the function return False
def valuesGreaterThanSecond(list):
    new_list = []
    secondValue = list[2]
    
    for x in list:
        if x > secondValue:
            new_list.append(x)
    
    print(len(new_list))
    
    if len(new_list) < 2:
        return False
    else:
        return new_list
    
print(valuesGreaterThanSecond(list_1))

# Write a function that accepts two integers as parameters:
# size and value. The function should create and return a
# list whose length is equal to the given size, and whose
# values are all the given value.
def thisLength_ThatValue(size, value):
    
    new_list = [value] * size
    print(new_list)
    
print(thisLength_ThatValue(4,7))