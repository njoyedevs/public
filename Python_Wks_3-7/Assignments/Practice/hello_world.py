# importing module
import traceback

import logging
logger=logging.getLogger()

# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello",name) # with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",str(name))	# with a comma
try:
    print("Hello" + name)	# with a +	-- this one should give us an error!
except TypeError as t:
    # print(f"There was a TypeError due to: {t}")
    logger.exception("Exception Occured while code Execution ======>\n")
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

x = [5,34,10,1,6]

print(x)
x.append(2)
print(x)

if not x: 
    print(True)
else:
    print(False)