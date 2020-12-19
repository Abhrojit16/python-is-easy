#if.py

"""
Homework Assignment #3: "If" Statements

"""

# compare three values, return true only if 2 or more values are true

#input
status = "single"
profession = "Designer"
age = 25

#output
happy = True
happy = False

#if statement
if status == "single" and profession == "Designer" and age >= 25:
	happy = True

elif status == "single" and profession == "Designer" or age >= 25 and profession == "Designer" or age >= 25 and status == "single":
	happy = True
    
else:
	happy = False
    
print ("Are you happy?")
print (happy)



"""
Bonus:
Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.

"""

def compare (a, b, c):
	if int(a)==int(b) or int(a)==int(c) or int(b)==int(c):
		return True
    else:
    	return False

print(compare(5, 6, 5)) #True
print(compare(5, 6, "5")) #True
print(compare(5, 6, 8)) #False
