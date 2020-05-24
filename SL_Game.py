import Die
import SL_Board
import Player

def main():
	# Your code goes here
	# Yu WU 
	# V00917423
	# 12/3/2018
	print("\n\nSNAKES AND LADDERS")
	print("\nThe board")
	
	
	Player1 = Player.Player()
	Player2 = Player.Player()
	
	# Use mutator method(s) of the Player class to change the players’ names to Aaron and Quinn. 
	Player1.set_name("Aaron")
	Player1.set_symbol()
	Player1.set_position(1)
	
	Player2.set_name("Quinn")
	Player2.set_symbol()
	Player2.set_position(1)
	
	
	# Make sure the two player’s symbols are different. Change one if needed using a mutator method of the Player class. 
	while Player1.get_symbol() == Player2.get_symbol():
		Player1.get_symbol()

	# Print the full board to the output.
	board = boardData()
	print(board)
	
	# Print out the full information for both players, in the following format.
	
	print("Player 1 = ",Player1)
	print("Player 2 = ",Player2)
	snake_location,ladder_location = SpecialLocation()
	
	position1 = 0
	position2 = 1
	
	# Call the function to change the player’s position on the board
	# Print out the full information for the player, using format: name (symbol): position. 
	while position1 < 36 and position2 < 36:
		
		position1 += GameTurn(snake_location,ladder_location,1)
		
	# If the position is greater than the length of the board, the position should be changed to the last square on the board. 
		if position1 > 36:
			position1 = 36
		Player1.set_position(position1)
		
		position2 += GameTurn(snake_location,ladder_location,0)
		if position2 > 36:
			position2 = 36
		Player2.set_position(position2)
		
		
		print(Player1)
		print(Player2)
	

	# The first player that ends the turn on the last square of the board is declared the winner.
	# Print out the word WINNER, followed by the name and symbol of the winning player. 	
	if position1 == 36:
		print("WINNER"+" Aaron "+Player1.get_symbol())
	else:
		print("WINNER"+" Quinn "+Player2.get_symbol())		
			
			
			
#Add and document suitable functions
def SpecialLocation():
	with open ("boardConfig.txt","r")as f:
        
        # Size representing the number of rows and columns on the board. 
		size = f.readline(1)

		# Second line contains pairs of numbers represents the location of the head and the location of the tail of a snake on the board.
		pairs = f.readlines(2)
		while "\n" in pairs:
			pairs.remove("\n")

		pairs = pairs[0].split()

		snake_location = []
		for i in range(0,len(pairs),2):
			pair = tuple(pairs[i:i+2])
			snake_location.append(pair)

		snake_location = tuple(snake_location)
		snake_location = dict(snake_location)



		# Third line contains pairs of numbers represents the locations of the bottom and the location of the top of a ladder on the board.
		pairs2 = f.readlines(3)
		while "\n" in pairs:
			pairs.remove("\n")

		pairs2 = pairs2[0].split()

		ladder_location = []
		for i in range(0,len(pairs2),2):
			pair = tuple(pairs2[i:i+2])
			ladder_location.append(pair)
			
		ladder_location = tuple(ladder_location)
		ladder_location = dict(ladder_location)
	
		return snake_location,ladder_location
		
		
		
def GameTurn(snake,ladder,position):
	
	# A turn starts with a throw of the die. 
	Dice = Die.Die()
	Dice.throw()
	
	# Change the player’s position on the board.
	# Add the value of the die throw to the player’s current position.
	Move = Dice.get_faceUp()
	position = position + Move
	
	# If there is the head of a snake or the bottom of a ladder on that square of the board, the position to is updated appropriately. 
	if position in snake:
		position = snake[position]
	elif position in ladder:
		positon = ladder[position]
	else:
		return position
		
		
		
#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()