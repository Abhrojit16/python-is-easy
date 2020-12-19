"""
You're about to do an assignment called "Fizz Buzz", which is one of the classic programming challenges. It is a favorite for interviewers, and a shocking number of job-applicants can't get it right. But you won't be one of those people. Here are the rules for the assignment (as specified by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

"""

def PrintFizBuzz():

	#printing 1 right away becuas eit is not a prime number

	for num in range(1 , 101):

		if num == 1:
			print(num)
			continue

		#Global varialbles: True or False associated with Prime Number
		Prime_t = True
		Prime_f = False

		#checking whether the number is prime or not. 
		#In order to be a prime number the number cannot be divisible by any number from (and including 2) up to that number

		for prime in range (2, num):
			if num%prime == 0:
				Prime_f == False
				break #if it is not a prime number it will still have to go through the next if , elif, else loops

			#if number is not divisible by any number from 2 upto that number then it is a prime number.
			else:
				print(num, "is a prime number.")


		if num%3 == 0 and num%5 == 0:
			print("FizzBuzz" , "=" , num)
			break

		elif num%3 == 0:
			print("Fizz" , "=" , num)
			break
		
		elif num%5 == 0:
		 	print("Buzz" , "=" , num)
			break

		else:
			Prime_f == False
			print(num)

PrintFizBuzz()

