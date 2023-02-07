# 1. Update Values in Dictionaries and Lists
#      1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#      2. Change the last_name of the first student from 'Jordan' to 'Bryant'
#      3. In the sports_directory, change 'Messi' to 'Andres'
#      4. Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# 1
for val_1 in range(len(x)):
    
    subVal_1 = x[val_1]
    
    for val_2 in range(len(subVal_1)):
        
        subVal_2 = subVal_1[val_2]
        
        if subVal_2 == 10:
            x[val_1][val_2] = 15
print(x)

# 2
for val_1 in range(len(students)):
    
    students_copy = students[val_1].copy()
    
    subVal_1 = students_copy
    
    if subVal_1["last_name"] == "Jordan":
        subVal_1["last_name"] = "Bryant"
        print(subVal_1)


# 3 
for val_1 in list(sports_directory.keys()):
    if val_1 == "soccer":
        for idx, val_2 in zip(range(len(sports_directory[val_1])),list(sports_directory[val_1])):
            if val_2 == "Messi":
                # print(val_2)
                sports_directory[val_1][idx] = "Andres"
print(sports_directory)

# 4
for dicts in range(len(z)):
    for val, key in zip(z[dicts].values(),list(z[dicts].keys())):
        # print(val)
        # print(key)
        if val == 20:
            # print(val)
            # print(key)
            z[dicts][key] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that,
# given a list of dictionaries, the function loops through
# each dictionary in the list and prints each key and the
# associated value. For example, given the following list:
def iterateDictionary(input_list):
    
    for dicts in range(len(input_list)):
        
        first = ""
        last = ""
        
        count = 0
        
        for val, key in zip(input_list[dicts].values(),list(input_list[dicts].keys())):
            # print(val)
            # print(key)
            
            if count ==0:
                first = f"{key} - {val}"
                count += 1
            elif count ==1:
                last = f"{key} - {val}"
                count -= 1
            
        print(f"{first}, {last}")

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list)
# that, given a list of dictionaries and a key name, the
# function prints the value stored in that key for each
# dictionary. For example, iterateDictionary2('first_name', students)
# should output:
def iterateDictionary2(key_name, some_list):

    for x in some_list:
        print(x[key_name])
        
iterateDictionary2("first_name", students)

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given
# a dictionary whose values are all lists, prints the
# name of each key along with the size of its list, and
# then prints the associated values within each key's list.
# For example:
def printInfo(some_dict):
    
    for key,value in some_dict.items():
        print([key, len(value), value])
printInfo(sports_directory)
