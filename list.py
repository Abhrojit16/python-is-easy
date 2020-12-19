"""
Create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. 
If the value doesn't exist already, it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;

"""
#My list 
MyUniqueList = []

#The left over list
MyLeftOvers = []

def AddToList(Input):
	if Input in MyUniqueList:
		MyLeftOvers.append(Input)
    return False
    print("This already there in the list!")
    
    else:
    	MyUniqueList.append(Input)
    return True

"""
Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called 
myLeftovers. If someone tries to add a value to myUniqueList but it's rejected 
(for non-uniqueness), it should get added to myLeftovers instead.


"""

def AddToList(Input):
	if Input in MyUniqueList:
		MyLeftOvers.append(Input)
    
    
    
Print(AddToList("Ab"))
Print(MyUniqueList)

Print(AddToList("Ab"))
Print(MyUniqueList)
Print(MyLeftOvers)

Print(AddToList("Tree"))
Print(MyUniqueList)
Print(MyLeftOvers)

Print(AddToList("Hello"))
Print(MyUniqueList)
Print(MyLeftOvers)

Print(AddToList("Tree"))
Print(MyUniqueList)
Print(MyLeftOvers)