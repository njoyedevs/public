num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #
print(type(fruit)) # log statement  # type check
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # Tuples add value
print(person['name']) # log statement
person['name'] = 'George' # variable declaration
person['eye_color'] = 'blue' # variable declaration
print(fruit[2]) # log statement

if num1 > 45: # conditional if else
    print("It's greater") # log statement
else:
    print("It's lower") # log statement

if len(string) < 5: #  conditional if elif else # length of string
    print("It's a short word!") # log statement
elif len(string) > 15: # length of string
    print("It's a long word!") # log statement
else:
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): # for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # increment variable by 1

pizza_toppings.pop() # List delete value
pizza_toppings.pop(1) # List delete value 1

print(person) # log statement
person.pop('eye_color') # List delete value eye_color
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if 
        continue # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives':  # conditional if 
        break # break

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # functino call

def print_hello_x_times(x): # function
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # functino call
print_hello_x_or_ten_times(4) # functino call


"""
Bonus section
"""

print(num3) # log statement
num3 = 72  # variable declaration
fruit[0] = 'cranberry' # variable declaration
print(person['favorite_team'])   # log statement
print(pizza_toppings[7])  # log statement
print(boolean)  # log statement
fruit.append('raspberry')  # Tuples add value
fruit.pop(1) # List delete value