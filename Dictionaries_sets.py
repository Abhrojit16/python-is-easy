"""
Details:
Return to your first homework assignments, when you described your favorite song.
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through 
each item in the dictionary and prints out it's key and then it's value.

"""

My_Favourite_song = {
"Title" : "My favourite song", 
"Song_name" : "Another Brick in the Wall",
"Artist" : "Pink Floyd",
"NumberOfParts" : "3",
"Genre1" : "pop",
"Genre2" : "Progressive rock",
"Album" : "The Wall",
"Label" : "Harvest",
"Producers" : " Bob Ezrin, David Gilmour, James Guthrie, Roger Waters",
"RedeasedDate" : "30th December",
"RedeasedYear" : "1979",
"Awards" : "Juno Award for International Single of the Year & BAFTA Best Original Song Written for a Film",
}


def My_song_details():
	print("\nThe Details of my favourite song:\n")
	for key in My_Favourite_song:
		print(key , ":" , My_Favourite_song[key])
	print("\nThe end\n")

My_song_details()

"""
Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, 
and find out if they were right or wrong. This function should accept two parameters: 
Key and Value. If the key exists in the dictionary and that value is the correct value, 
then the function should return true. In all other cases, it should return false.

"""

def Guess_my_Song():
	while(True):
		key1 = print(input("\nLets play a game! \nGuess the key:\n"))
		value1 = print(input("\nNow, guess the value:\n"))
		key2 = key1.lower()
		value2 = value1.lower()

		if key2 in My_Favourite_song.lower():
			if My_Favourite_song[].lower() == value2:
				print("\nYou are correct! Try again:\n")

			else:
				print("\nSorry you have entered a wrong value!!! Try again?\n")
		
		else:
			print("\nSorry you have entered a wrong key or value!!! Try again?\n")


Guess_my_Song()

