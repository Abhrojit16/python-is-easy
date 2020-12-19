passOrFail.py

NumberOfPass = []
NumberOfFail =[]

Pass = 0
Fail = 0

for num in range(40,101):
	print("Pass")
	NumberOfPass.append(num)
	Pass += 1

else:
	print("fail")
	NumberOfFail.append(num)
	Fail += 1


print(NumberOfPass)
print(NumberOfFail)
print(Pass)
print(Fail)