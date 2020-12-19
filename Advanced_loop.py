"""
Create a function that takes in two parameters: rows, and columns, 
both of which are integers. The function should then proceed to draw a 
laying board (as in the examples from the lectures) the same number of 
rows and columns as specified. After drawing the board, your function should return True.

"""


def advanced_loops (rows , columns):

	max_rows = 1200
	max_cols = 1200
	rows = int(rows)
	columns = int(columns)

	if rows<=max_rows and columns<=max_cols:
		for r in range(1, rows+1):
			if r%2 != 0:
				for c in range(1, columns+1):
					if c%2 != 0:
						if c==columns+1:
							print("")

						else:
							print(" " , end="")

					else:
						if c==columns+1:
							print("")

						else:
							print("|", end= "")

			else:
				print("-"*columns)

		return True

	else:

		print("Sorry the value you have entered is more than the maximum rows and columns you can enter. Maximum rows: 1200 and Maximum columuns: 1200")
		return False


advanced_loops(50,90)

advanced_loops(1300 , 1400)