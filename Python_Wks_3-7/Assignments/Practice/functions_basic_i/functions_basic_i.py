#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# 5

#2
try:
    def number_of_military_branches():
        return 5
    print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# NameError There is no function called number_of_days_in_a_week_silicon_or_triangle_sides
except NameError as n:
    print("\n<<=============>>\nException: NameError\n" + f"{n}\n<<=============>>\n") 
    pass

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# 5 


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# there would be 1 print on line 31.  Line 33 would be none as the value
# of number_of_great_lakes was not set with return. Therefore, x will not be given a value

#6
try:
    def add(b,c):
        print(b+c)
    print(add(1,2) + add(2,3))
except TypeError as t:
    print("\n<<=============>>\nException: TypeError\n" + f"{t}\n<<=============>>\n") 
    pass
    
# There would be a TypeError due to adding NoneTypes in line 44.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Print on link 47 would print "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Line 53 would print 100.  b >= 10 so the else would return 10.  The return on line 58
# does not execute regardless as it is outside of all possible if/else.  The Print on
# line 58 would print 10.


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Printiung this function will never execute line 71.  Printing with (2,3) as argument
# will execute the if satement and return 7 thusly printing 7 on line 72.
# Printing with (5,3) would execute the else statment return 14 thusly printing 14 on linke 73.
# Printing both previous statements while adding with + would print 98. 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Printing addition() will never execute return 10.  Printing with addition(3,5) will
# return 8 thusly printing 8 on line 84.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Print on linke 91 would result in 500, as well as linke 95.  Linke 96 would print b which was 
# re-assigned on line 93 to 300 and printed by line 94.  Linke 97 would print 500.


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# 500 (Line 104), 500 (line 109), 300 (line 107) return 300 and returned to value for line 110.
# 300 (line 111)

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500500300300 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 132

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 13510